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
            await asyncio.sleep(1)
            await websocket.send(json.dumps({
                'command': 'click',
                'x': 30,
                'y': 0
                # this should be somewhat right of the player
                # because we send this right after the game starts
                # (0,0) is the middle of the field
                # we need to calculate these commands based on the position of the player
                # who is the cell at position 0 in the cells list
            }))

start_server = websockets.serve(hello, 'localhost', 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
