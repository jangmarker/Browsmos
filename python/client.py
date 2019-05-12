#!/usr/bin/python3

import asyncio
import websockets
import json
from aioconsole import ainput

async def hello(websocket, path):
    async for message in websocket:
        msg = json.loads(message)
        print(msg)
        if msg['type'] == 'lost':
            await ainput("press ok to restart")
            await websocket.send(json.dumps({
                'command': "start"
            }))

start_server = websockets.serve(hello, 'localhost', 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
