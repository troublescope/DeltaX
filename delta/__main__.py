import asyncio
import uvloop
from .loader import setup_logging, main

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


if __name__ == "__main__":
    setup_logging()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
