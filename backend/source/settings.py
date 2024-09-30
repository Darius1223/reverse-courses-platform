import structlog
import pydantic
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


pydantic.BaseSettings = BaseSettings
logger: structlog.stdlib.BoundLogger = structlog.get_logger()


class AuthSettings(BaseModel):
    secret_key: str
    algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=30)


class SmtpSettings(BaseModel):
    email: str
    password: str


class RedisSettings(BaseModel):
    url: str


class Settings(BaseSettings):
    database_url: str = Field()

    auth: AuthSettings
    smtp: SmtpSettings
    redis: RedisSettings

    model_config = SettingsConfigDict(env_nested_delimiter="__", env_file=".env")


settings = Settings()
logger.debug(settings)
