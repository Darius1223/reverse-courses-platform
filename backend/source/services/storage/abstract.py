import abc

from source.services.abstract import AbstractService


class StorageService(AbstractService, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    async def set_value(self, key: str, value: str):
        pass
