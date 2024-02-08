from .base import Base
from sqlalchemy import String, Column, Integer, Boolean


class Todo(Base):
    __tablename__ = "todos"
    title = Column(String)
    completed = Column(Boolean, default=False)
