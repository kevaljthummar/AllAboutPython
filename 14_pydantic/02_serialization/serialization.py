from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="KT",
    email="kt@test.com",
    createdAt=datetime(2024, 3, 15, 14, 30, 20),
    address= Address(
        street="test test",
        city="st",
        zip_code="1234546"
    ),
    is_active=False,
    tags=["PU","Subscriber"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)

json_str = user.model_dump_json()
print("="*30)
print(json_str)