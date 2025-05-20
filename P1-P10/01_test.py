from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    'signup_ts': '2019-06-01 12:00',
    'friends': [1, 2, '3']
}

user = User(**external_data)
print(user.id)
print(repr(user.signup_ts))
print(user.friends)
print(user.name)
print("---------------------------------")
print(user)
print(user.model_dump())