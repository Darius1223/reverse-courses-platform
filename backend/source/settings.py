import structlog
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class Auth(BaseModel):
    secret_key: str
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)


class Settings(BaseSettings):
    database_url: str = Field()

    auth: Auth

    model_config = SettingsConfigDict(env_nested_delimiter="__", env_file=".env")


settings = Settings()
logger.debug(settings)
