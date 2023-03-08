import asyncio
from typing import Optional

from aiopath import AsyncPath
import logging

from .config import Config
from .delta import Delta
from .logging import AsyncLogger
from .plugins import PluginManager

plugin_manager = PluginManager("plugins")

def setup_logging() -> None:
    # Set up the root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Set up the Delta logger
    delta_logger = AsyncLogger("Delta")
    delta_logger.setLevel(logging.INFO)
    logging.getLogger("pyrogram").setLevel(logging.WARNING)
    # Add the Delta logger to the root logger
    logging.getLogger().addHandler(delta_logger)


async def main() -> None:
    delta = Delta(
        name="DeltaBot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugin_manager=plugin_manager,
    )