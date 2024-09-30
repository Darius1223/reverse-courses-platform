from datetime import timedelta
from typing import Annotated

import structlog.stdlib
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from source.backends.auth import Token, AuthBackend
from source.containers import Container
from source.database.models import User
from source.schemas.user import RegistrationsRequestForm
from source.settings import settings

auth_router = APIRouter(prefix="/auth")
logger: structlog.stdlib.BoundLogger = structlog.get_logger(module="auth")


@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_backend: AuthBackend = Depends(Provide[Container.auth_backend]),
) -> Token:
    user = await auth_backend.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.auth.access_token_expire_minutes)
    access_token = auth_backend.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@auth_router.post("/registration")
@inject
async def registration(
    form_data: Annotated[RegistrationsRequestForm, Depends()],
    auth_backend: AuthBackend = Depends(Provide[Container.auth_backend]),
) -> User:
    logger.debug("Start registration user", form_data=form_data)

    user = await auth_backend.registration(form_data)

    return user
