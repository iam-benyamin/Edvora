from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
socket_manager = SocketManager(app=app)


@app.get("/")
def read_root():
    return {"Hi": "Hello, World!"}
