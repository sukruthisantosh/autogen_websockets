import client
import uvicorn
import asyncio


async def main():
    print("hello")
    config = uvicorn.Config(client.app)
    server = uvicorn.Server(config)
    await server.serve()  # noqa: F704

asyncio.run(main())
