import websocket, json
from config import *

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "authenticate",
        "data": {"key_id": API_KEY, "secret_key": SECRET_KEY}
    }

    ws.send(json.dumps(auth_data))
    listen_message = {"action": "listen", "data": {"streams": ["T.TSLA"]}}
    ws.send(json.dumps(listen_message))

def on_message(ws, message):
    print("received a message")
    print(message)

socket = "wss://paper-api.alpaca.markets/stream"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
