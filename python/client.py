#!/usr/bin/python3

import asyncio
import websockets
import json

async def hello(websocket, path):
    async for message in websocket:
        print(json.loads(message))

start_server = websockets.serve(hello, 'localhost', 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
