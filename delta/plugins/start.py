from pyrogram import filters

class StartPlugin:
    name = "start"

    @delta.on_message(filters.command("start"))
    async def start_command(self, client, message):
        await message.reply_text("Hello! I'm a Delta bot.")
