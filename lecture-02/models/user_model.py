from .base import Base
from sqlalchemy import String, Column, Integer


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))

    def __repr__(self):
        return "{} {} {}".format(self.id, self.name, self.email)

    def to_dict(self):
        return {
            "id" : self.id,
            "name": self.name,
            "email": self.email
        }
