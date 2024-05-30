# receiver_client.py
import asyncio
import websockets
import json
import time

class MessageReceiver:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def receive_messages(self, websocket):
        while True:
            message = await websocket.recv()
            message = json.loads(message)
            await self.queue.put(message)
            print(f'Received: {message}')

    async def display_messages(self):
        while True:
            if not self.queue.empty():
                message = await self.queue.get()
                print(f'Displayed: {message}')
                await asyncio.sleep(2)

    async def handler(self):
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as websocket:
            receiver_task = asyncio.create_task(self.receive_messages(websocket))
            display_task = asyncio.create_task(self.display_messages())
            await asyncio.gather(receiver_task, display_task)

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.handler())

if __name__ == "__main__":
    receiver = MessageReceiver()
    receiver.start()
