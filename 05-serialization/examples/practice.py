from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    is_active: bool = Field(default=True)
    createdAt: datetime
    address: Address
    tags: List[str] = []

    # model_config is used to configure the model
    model_config = ConfigDict(
        json_encoders = {datetime: lambda value : value.strftime('%d-%m-%Y %H:%M:%S'), email: lambda value : f"Modified by 'model_config' --> {value}"}
    )

# create a user instance
user = User(
    id= 1,
    name= "hitesh",
    email= "hitesh@hc.com",
    createdAt = datetime(2024, 3, 15, 14, 30),
    address= Address(
        street = "something",
        city = "Jaipur",
        zip_code = "001144"
    ),
    is_active = True,
    tags = ["premium", "subscriber"],
)

print(user.model_dump()) # obj.model_dump() returns dictionary
print("\n ------------------------------ \n")
print(user.model_dump_json()) # obj.model_dump_json() returns json string