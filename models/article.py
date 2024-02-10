from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime


class Article(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)

    title = Column(String(100), nullable=False)
    intro = Column(String(100), nullable=False)
    text = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.id}"