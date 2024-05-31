import asyncio
import websockets
import json
import queue

async def message_receiver(queue):
    print("Attempting to receive...")
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            print("Awaiting message...")
            message = await websocket.recv()
            queue.put_nowait(json.loads(message))
            await asyncio.sleep(1.5)

async def message_printer(queue):
    while True:
        if not queue.empty():
            message = queue.get_nowait()
            print(f"Received: {message}")
            await asyncio.sleep(2)
        else:
            await asyncio.sleep(0.1)

async def main():
    q = queue.Queue()
    message_receiver_task = asyncio.create_task(message_receiver(q))
    message_printer_task = asyncio.create_task(message_printer(q))
    
    await asyncio.gather(message_receiver_task, message_printer_task)

if __name__ == "__main__":
    print("Starting...")
    asyncio.run(main())
