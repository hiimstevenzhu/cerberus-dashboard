# receiver_client.py
import asyncio
import websockets
import json

class MessageReceiver:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def receive_messages(self, websocket):
        try:
            while True:
                print("Awaiting message...")
                message = await websocket.recv()
                print("Obtained message...")
                message = json.loads(message)
                await self.queue.put(message)
                print(f"Received a message, {message}")
        except websockets.ConnectionClosed as e:
            print(f"Connection closed: {e}")

    async def display_messages(self):
        while True:
            if not self.queue.empty():
                print("Displaying...")
                message = await self.queue.get()
                print(f'Displayed: {message}, count: {message}')
                await asyncio.sleep(2)

    async def handler(self):
        uri = "ws://localhost:8765"
        try:
            print(f"Connecting to {uri}")
            async with websockets.connect(uri) as websocket:
                print("Connected to server")
                receiver_task = asyncio.create_task(self.receive_messages(websocket))
                display_task = asyncio.create_task(self.display_messages())
                await asyncio.gather(receiver_task, display_task)
        except Exception as e:
            print(f"Failed to connect to server: {e}")

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.handler())

if __name__ == "__main__":
    print("Starting receiver...")
    receiver = MessageReceiver()
    receiver.start()
