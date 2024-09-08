from datetime import timedelta, datetime, timezone
from typing import TypeVar, Type, Generic

import jwt
import structlog.stdlib
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlmodel import select


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
_UserModel = TypeVar("_UserModel")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class AuthBackend(Generic[_UserModel]):
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        access_token_expire_minutes: int,
        session_maker: async_sessionmaker,
        user_model: Type[_UserModel],
    ):
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._access_token_expire_minutes = access_token_expire_minutes

        self._session_maker = session_maker

        self.user_model = user_model

        self._pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.logger: structlog.stdlib.BoundLogger = structlog.get_logger(module="auth")

    @property
    def pwd_context(self) -> CryptContext:
        return self._pwd_context

    @property
    def session_maker(self) -> async_sessionmaker:
        return self._session_maker

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
