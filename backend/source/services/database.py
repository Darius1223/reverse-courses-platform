from typing import TypeVar, Generic, Type

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlmodel import SQLModel

from source.services.abstract import AbstractService

_ModelType = TypeVar("_ModelType", bound=SQLModel)


class _ModelProvider(AbstractService, Generic[_ModelType]):
    def __init__(self, model: Type[_ModelType], session_maker: async_sessionmaker):
        super().__init__()
        self.session_maker = session_maker
        self.model = model

    async def create(self, object_: _ModelType) -> _ModelType:
        async with self.session_maker() as session:
            try:
                session.add(object_)
                await session.commit()

                await session.refresh(object_)

            except Exception as e:
                self.logger.error("Error while db query [create]")
                await session.rollback()
                raise e
            else:
                return object_


class DatabaseService(AbstractService):
    def __init__(self, session_maker: async_sessionmaker):
        super().__init__()
        self.session_maker = session_maker

    def __call__(self, model: Type[_ModelType]) -> _ModelProvider[_ModelType]:
        return _ModelProvider(model, self.session_maker)
