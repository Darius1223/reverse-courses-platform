import secrets
import string
from datetime import timedelta, datetime, timezone
from pathlib import Path
from typing import TypeVar, Type, Generic

import jwt
import structlog.stdlib
from fastapi.security import OAuth2PasswordBearer
from jinja2 import Template
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlmodel import select

from source.schemas.user import RegistrationsRequestForm
from source.services.database import DatabaseService
from source.services.smtp import SmtpService
from source.services.storage.abstract import StorageService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
_UserModel = TypeVar("_UserModel")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class AuthBackend(Generic[_UserModel]):
    EMAIL_SUBJECT = "Регистрация на платформе 'Педагогическая мастерская'"
    PASSWORD_LENGTH = 32
    HTMP_TEMPLATE = "templates/registration.html"

    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int,
        database_service: DatabaseService,
        user_model: Type[_UserModel],
        smtp_service: SmtpService,
        storage_service: StorageService,
    ):
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._access_token_expire_minutes = access_token_expire_minutes

        self._database_service = database_service


        self.user_model = user_model

        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        self.smtp_service = smtp_service
        self.storage_service = storage_service

        self.alphabet = string.ascii_letters + string.digits

        self.logger: structlog.stdlib.BoundLogger = structlog.get_logger(module="auth")


    @property
    def pwd_context(self) -> CryptContext:
        return self._pwd_context

    @property
    def database_service(self) -> DatabaseService:
        return self._database_service

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    async def get_user(self, username: str) -> _UserModel:
        async with self.session_maker() as session:
            stmt = select(self.user_model).where(self.user_model.username == username)
            result = (await session.execute(stmt)).first()
            user = result[0] if result else None
            self.logger.debug("Fetching user from db", user=user)

            return user

    async def authenticate_user(
        self, username: str, password: str
    ) -> _UserModel | None:
        user = await self.get_user(username)
        if not user:
            return None
        if not self.verify_password(password, user.password):
            return None
        return user

    def create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(
                minutes=self._access_token_expire_minutes
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self._secret_key, algorithm=self._algorithm)
        return encoded_jwt

    async def registration(self, form_data: RegistrationsRequestForm) -> _UserModel:
        password = self._generate_password()

        user = self.user_model(
            firstname=form_data.firstname,
            lastname=form_data.lastname,
            surname=form_data.surname,
            email=form_data.email,
            telephone=form_data.telephone,
            hashed_password=self.get_password_hash(password),
            role=form_data.role,
        )

        self.logger.debug("Create user", user=user)

        user_db = await self.database_service(self.user_model).create(user)
        self.logger.debug("Creating user", user_db=user_db)

        await self.smtp_service.send_mail(
            email_to=form_data.email,
            subject=self.EMAIL_SUBJECT,
            text=self._generate_text(
                first_name=form_data.firstname,
                password=password,
            ),
        )

        return user

    def _generate_text(self, first_name: str, password: str) -> str:
        file_path = Path.cwd() / self.HTMP_TEMPLATE
        with open(file_path, "r") as f:
            text = f.read()
        template = Template(text).render(password=password, username=first_name)
        return template

    def _generate_password(self) -> str:
        return "".join(
            secrets.choice(self.alphabet) for i in range(self.PASSWORD_LENGTH)
        )
