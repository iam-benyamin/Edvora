from fastapi import FastAPI
from fastapi_socketio import SocketManager
from sqlalchemy.orm import Session

from app.model.user import Base
from app.db.database import SessionLocal, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

# socket_manager = SocketManager(app=app)


@app.get("/")
def index():
    return {"Hi": "Hello, World!"}

