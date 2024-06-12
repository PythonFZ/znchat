from flask_socketio import SocketIO, emit
from flask import request
from znchat import tasks


def init_socketio_events(socketio: SocketIO):
    @socketio.on("connect")
    def handle_connect():
        emit("my_response", {"data": "Connected"})
        tasks.hello.delay(request.sid)

    @socketio.on("disconnect")
    def handle_disconnect():
        print("Client disconnected")

    @socketio.on("message")
    def message(msg: str):
        print(f"Message: {msg}")
        emit("message", msg, broadcast=True)
