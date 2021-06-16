from pydantic import BaseModel
from typing import List


class TagBase(BaseModel):
    value: str
    text: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        orm_model = True


class PlaceBase(BaseModel):
    name: str
    description: str
    station: str
    address: str
    rating_sum: float
    count_of_rate: int
    rate: float
    photo: str


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int
    categories: List[Tag] = []

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
