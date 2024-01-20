import os
from flask_sqlalchemy import SQLAlchemy
from app import app
from dotenv import load_dotenv



class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def repr(self):
        return f'<Article {self.id}'