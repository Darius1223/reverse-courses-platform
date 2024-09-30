from dependency_injector import providers, containers

from source.backends.auth import AuthBackend
from source.database.core import create_session
from source.database.models import User
from source.services.database import DatabaseService
from source.services.smtp import SmtpService
from source.services.storage.abstract import StorageService
from source.services.storage.redis import RedisStorageService
from source.settings import settings, Settings

from redis import asyncio as aioredis


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration(pydantic_settings=[settings])

    # sessions
    database_service = providers.Factory(DatabaseService, create_session)

    # services
    smtp_service: SmtpService = providers.Factory(
        SmtpService,
        email=config.smtp.email,
        password=config.smtp.password,
    )

    # redis
    redis: aioredis.Redis = providers.Singleton(
        aioredis.Redis.from_url,
        url=config.redis.url,
    )
    storage_service: StorageService = providers.Singleton(
        RedisStorageService,
        redis=redis,
    )

    # backends
    auth_backend: AuthBackend[User] = providers.Factory(
        AuthBackend,
        secret_key=settings.auth.secret_key,
        algorithm=settings.auth.algorithm,
        access_token_expire_minutes=settings.auth.access_token_expire_minutes,
        database_service=database_service,
        user_model=User,
        smtp_service=smtp_service,
        storage_service=storage_service,
    )


container = Container()
