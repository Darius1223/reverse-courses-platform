from source.services.storage.abstract import StorageService
from redis import asyncio as aioredis


class RedisStorageService(StorageService):
    def __init__(self, redis: aioredis.Redis):
        super().__init__()

        self.redis = redis

    async def set_value(self, key: str, value: str):
        return await self.redis.set(
            name=key,
            value=value,
        )
