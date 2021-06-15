from sqlalchemy import Boolean, Column, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)

    favorites = relationship("Place")


class Place(Base):
    __tablename__ = "places"
    name = Column(String)
    description = Column(String)
    station = Column(String)
    address = Column(String)
    rating = Column(Float)
    photo = Column(String)
