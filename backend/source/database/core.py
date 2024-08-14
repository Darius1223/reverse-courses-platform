from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from source.settings import settings

engine = create_async_engine(
    settings.database_url,
    echo=True,
)

session_maker = async_sessionmaker(engine)


async def create_session():
    async with session_maker() as session:
        yield session
