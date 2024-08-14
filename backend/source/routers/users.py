import structlog
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from source.database.core import create_session
from source.database.models import User
from source.schemas.user import UserSchema

users_router = APIRouter(prefix="/users", tags=["users"])
logger: structlog.stdlib.BoundLogger = structlog.get_logger(module="users_logger")


@users_router.get("/all")
async def get_users(
    session: AsyncSession = Depends(create_session),
) -> list[UserSchema]:
    stmt = select(User).order_by(User.id)

    cursor = await session.execute(stmt)

    users_raw = cursor.fetchall()
    users = [user for (user,) in users_raw]

    return users


@users_router.post("/")
async def create_user(
    user: UserSchema,
    session: AsyncSession = Depends(create_session),
) -> dict:
    logger.debug("Create user", user=user, db=session)

    stmt = insert(User).values(**user.model_dump())

    await session.execute(stmt)
    await session.commit()

    return {"health": True}
