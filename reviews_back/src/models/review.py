from sqlalchemy import Column, Integer, String
from src.config.db_settings import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column(String, primary_key=True, index=True)
    text = Column(String)
    score = Column(Integer)