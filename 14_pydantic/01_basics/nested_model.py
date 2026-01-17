from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="123 abc",
    city="surat",
    postal_code="123456"
)

user = User(
    id=1,
    name="KT",
    address=address
)

user_data = {
    "id": 1,
    "name": "KT",
    "address": {
        "street": "123 abc",
        "city": "surat",
        "postal_code": "123456",
    }
}

user = User(**user_data)
print(user)
