from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    hashed_password = Column(String)

    favorites = relationship("Place")


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    station = Column(String, nullable=False)
    address = Column(String)
    rating_sum = Column(Float)
    count_of_rate = Column(Integer)
    rate = Column(Float)
    photo = Column(String, nullable=False)

    tags = relationship('Tag')


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    text = Column(String)



