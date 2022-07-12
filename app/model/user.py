""" my user model with column id, username, first_name, last_name """
from sqlalchemy import Column, Integer, String

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String)

    def __repr__(self):
        return f"id:{self.id}, username:{self.username}, " \
               f"name:{self.first_name}, surname:{self.last_name}"
