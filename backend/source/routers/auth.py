from datetime import timedelta
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from source.backends.auth import Token, AuthBackend
from source.database.core import session_maker
from source.database.models import User
from source.settings import settings

auth_router = APIRouter(prefix="/auth")


auth_backend: AuthBackend[User] = AuthBackend(
    secret_key=settings.auth.secret_key,
    algorithm=settings.auth.algorithm,
    access_token_expire_minutes=settings.auth.access_token_expire_minutes,
    session_maker=session_maker,
    user_model=User,
)


@auth_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
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
