from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Keval Thummar"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000,
        le=1000000,
        description="Annual salary in USD"
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r'/^([A-Z|a-z|0-9](\.|_){0,1})+[A-Z|a-z|0-9]\@([A-Z|a-z|0-9])+((\.){0,1}[A-Z|a-z|0-9]){2}\.[a-z]{2,3}$/gm'
    )
    phone: str = Field(
        ...,
        regex=r'/^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$/gm'
    )
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )