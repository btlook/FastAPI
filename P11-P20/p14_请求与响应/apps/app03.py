from datetime import datetime, date

from fastapi import APIRouter
from typing import Union, Optional, List

from pydantic import BaseModel, Field, validator, field_validator

# Optional[str] = Union[str, None]

app03 = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    # name: str = Field(pattern="^s")
    name: str
    age: int = Field(default=0, gt=10, lt=20)
    birthday: date
    friends: List[int]
    description: Optional[str] = "我是一个描述"
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alphanumeric"
        return value


class Data(BaseModel):
    date: List[User]


@app03.post("/user")
async def user(user: User):  #
    print(user, type(user))
    print(user.name, user.age, user.birthday, user.friends)
    print(user.model_dump())
    return user


@app03.post("/data")
async def data(data: Data):
    print(data)
    return data
