import asyncio
from typing import Optional
from aiopath import AsyncPath
from pyrogram import Client
from .plugins import PluginManager


class Delta(Client):
    def __init__(
        self,
        name: str,
        *,
        api_id: int,
        api_hash: str,
        bot_token: str,
        plugin_manager: Optional[PluginManager] = None,
        in_memory: bool = False,
    ) -> None:
        super().__init__(
            name,
            bot_token=bot_token,
            api_hash=api_hash,
            api_id=api_id,
            workdir="delta",
            sleep_threshold=180,
            plugins={"root": "delta.plugins"},
        )
        self.plugin_manager = plugin_manager

    async def start(self) -> None:
        path: AsyncPath = AsyncPath("./downloads/")
        if not await path.is_dir():
            await path.mkdir(parents=True)

        if self.plugin_manager:
            self.plugin_manager.load_all_plugins()

        await super().start()  # Connect to telegram's servers

    async def stop(self) -> None:
        await super().stop()
