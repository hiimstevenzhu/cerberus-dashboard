import asyncio
import websockets
import json
import queue
from your_keyword_algorithm import search_keywords  # Import your keyword-searching algorithm

# Queue for incoming messages from speech recognition
incoming_queue = queue.Queue()
# Queue for outgoing messages to React
outgoing_queue = asyncio.Queue()

async def incoming_message_receiver(queue):
    print("Starting incoming WebSocket server...")
    async with websockets.serve(lambda ws, path: handle_incoming_message(ws, path, queue), "localhost", 8765):
        print("Incoming WebSocket server started on port 8765.")
        await asyncio.Future()  # run forever

async def handle_incoming_message(websocket, path, queue):
    print("Speech recognition client connected.")
    try:
        async for message in websocket:
            queue.put_nowait(json.loads(message))
            print(f"Received message from speech recognition, putting into queue...")
    except websockets.exceptions.ConnectionClosedError:
        print("Speech recognition client disconnected.")

async def outgoing_message_sender():
    print("Starting outgoing WebSocket server...")
    async with websockets.serve(handle_outgoing_connection, "localhost", 8766):
        print("Outgoing WebSocket server started on port 8766.")
        await asyncio.Future()  # run forever

async def handle_outgoing_connection(websocket, path):
    print("React client connected.")
    try:
        while True:
            message = await outgoing_queue.get()
            await websocket.send(json.dumps(message))
            print(f"Sent message to React: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("React client disconnected.")

async def message_processor():
    while True:
        if not incoming_queue.empty():
            message = incoming_queue.get_nowait()
            print(f"Processing message: {message['message']}")
            
            # Apply your keyword-searching algorithm here
            processed_message = search_keywords(message['message'])
            
            # Put the processed message in the outgoing queue
            await outgoing_queue.put(processed_message)
        else:
            await asyncio.sleep(0.1)

async def main():
    incoming_receiver_task = asyncio.create_task(incoming_message_receiver(incoming_queue))
    outgoing_sender_task = asyncio.create_task(outgoing_message_sender())
    processor_task = asyncio.create_task(message_processor())
    
    await asyncio.gather(incoming_receiver_task, outgoing_sender_task, processor_task)

if __name__ == "__main__":
    print("Starting...")
    asyncio.run(main())