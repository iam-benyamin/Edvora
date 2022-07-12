# Task

create an authenticated feed system using FastAPI and Socket.IO.

- [X] best practics for project structure
- [X] create database (sqlalchemy)
- [X] create user model
- [ ] login functionality
- [ ] logout functionality
- [ ] session management
- [ ] should be broadcasted to all authenticated users connected via websockets.


# Start project

make virtual enviroment \
``` python3 -m venv env ```

activate enviroment \
``` source env/bin/activate ```

install requirements \
``` pip3 install -r requirements.txt ```

run app \
``` uvicorn app.main:app ```


# database

for data base I use sqlite3 and sqlalchemy

