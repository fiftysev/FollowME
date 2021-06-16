from pydantic import BaseModel
from typing import List


class PlaceBase(BaseModel):
    name: str
    description: str
    station: str
    address: str
    rating_sum: float
    count_of_rate: int
    rate: float


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    class Config:
        orm_model = True


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    favorites: List[Place] = []

    class Config:
        orm_model = True
