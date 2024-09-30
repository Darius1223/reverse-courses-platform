import structlog.stdlib


class AbstractBackend:
    def __init__(self):
        self._logger: structlog.stdlib.BoundLogger = structlog.get_logger(
            module=self.__class__.__name__
        )

    @property
    def logger(self) -> structlog.stdlib.BoundLogger:
        return self._logger
