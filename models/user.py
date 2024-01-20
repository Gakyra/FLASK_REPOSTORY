from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from datetime import datetime


class User():
    id = Column(Integer, primary_key=True)
    username = dColumn(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}"