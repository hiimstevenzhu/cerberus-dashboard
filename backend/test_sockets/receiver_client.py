import asyncio
import websockets
import json
import queue

async def message_receiver(queue):
    print("Starting WebSocket server...")
    async with websockets.serve(lambda ws, path: handle_message(ws, path, queue), "localhost", 8765):
        print("WebSocket server started.")
        while True:
            await asyncio.sleep(1)

async def handle_message(websocket, path, queue):
    print("Client connected.")
    while True:
        try:
            message = await websocket.recv()
            queue.put_nowait(json.loads(message))
            print(f"Received message, putting into queue...")
        except websockets.exceptions.ConnectionClosedError:
            print("Client disconnected.")
            break

async def message_printer(queue):
    while True:
        if not queue.empty():
            message = queue.get_nowait()
            print(f"Received from queue: {message['message']}")
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
