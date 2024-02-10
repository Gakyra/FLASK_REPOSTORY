from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}"