import structlog
from pydantic import Field
from pydantic_settings import BaseSettings

logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class Settings(BaseSettings):
    database_url: str = Field()


settings = Settings()
logger.debug(settings)
