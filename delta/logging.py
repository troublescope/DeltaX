import logging
import asyncio
from typing import Optional


class AsyncLogger(logging.Logger):
    def __init__(
        self,
        name: str,
        level: int = logging.NOTSET,
        *,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        debug: bool = False,
    ):
        """
        Create a new AsynLogger object.

        :param name: The name of the logger.
        :param level: The log level for the logger.
        :param loop: An event loop to use. If None, the default event loop will be used.
        :param debug: Whether to enable debug mode.
        """
        super().__init__(name, level)
        self.loop = loop or asyncio.get_event_loop()
        self.debug = debug

    async def log(self, level: int, msg: str, *args, **kwargs):
        """
        Log a message with the specified log level.

        :param level: The log level.
        :param msg: The message to log.
        :param args: Additional positional arguments to pass to the logging method.
        :param kwargs: Additional keyword arguments to pass to the logging method.
        """
        if self.isEnabledFor(level):
            if self.debug:
                func = getattr(self.loop, 'debug', None)
                if func is not None:
                    func(f'{self.name} - {msg}')
            await self.loop.run_in_executor(None, self._log, level, msg, args, **kwargs)

    async def debug(self, msg: str, *args, **kwargs):
        """
        Log a message with the DEBUG log level.

        :param msg: The message to log.
        :param args: Additional positional arguments to pass to the logging method.
        :param kwargs: Additional keyword arguments to pass to the logging method.
        """
        await self.log(logging.DEBUG, msg, *args, **kwargs)

    async def info(self, msg: str, *args, **kwargs):
        """
        Log a message with the INFO log level.

        :param msg: The message to log.
        :param args: Additional positional arguments to pass to the logging method.
        :param kwargs: Additional keyword arguments to pass to the logging method.
        """
        await self.log(logging.INFO, msg, *args, **kwargs)

    async def warning(self, msg: str, *args, **kwargs):
        """
        Log a message with the WARNING log level.

        :param msg: The message to log.
        :param args: Additional positional arguments to pass to the logging method.
        :param kwargs: Additional keyword arguments to pass to the logging method.
        """
        await self.log(logging.WARNING, msg, *args, **kwargs)
