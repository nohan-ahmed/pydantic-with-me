from re import I
from statistics import quantiles
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    EmailStr,
    ConfigDict,
    field_validator,
    model_validator,
    computed_field,
)
from typing import Optional, List, Dict
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    profiel_image: Optional[str] = None
    age: int = Field(..., ge=18, description="Age of the user", example=25)
    email: EmailStr = Field(
        ..., description="Email of the user", example="user@example.com"
    )
    phone: Optional[str] = Field(
        None, description="Phone number of the user", example="1234567890"
    )
    is_active: bool = Field(
        True, description="Active status of the user", examples=True
    )
    birth_date: datetime
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="hitesh",
    profiel_image="https://example.com/profile.jpg",
    age=25,
    email="hitesh@hc.com",
    birth_date=datetime(2024, 3, 15, 14, 30),
)

print("\n=============================\n")
print(user.model_dump())
print("\n=============================\n")
print(user.model_dump_json())
print("\n=============================\n")


class SingUp(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str

    @field_validator("username")
    def validate_password(
        cls, value
    ):  # field_validator takes two arguments, cls and value --> raise exeption or Validated data.
        if "sex" in value.lower():
            raise ValueError("Username cannot contain 'sex'")
        return value

    @model_validator(mode="after")
    def validate_passwords_match(cls, values):
        if not values.password:
            raise ValueError("Password is required")

        if not values.confirm_password:
            raise ValueError("Confirm password is required")

        if len(values.password) < 8 or len(values.confirm_password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values


signup = SingUp(
    username="se'xama if",
    email="hitesh@hc.com",
    password="12345678",
    confirm_password="12345678",
)

print("\n=============================\n")
print(signup.model_dump())
print("\n=============================\n")
print(signup.model_dump_json())
print("\n=============================\n")


class Product(BaseModel):
    id: int
    name: str
    image: Optional[str] = None
    price: float = Field(
        ..., ge=10, le=10000, description="Price of the product", example=99.99
    )

    quantiles: int

    @computed_field
    @property
    def total_price(self)->float:
        return self.price * self.quantiles


product = Product(
    id=1,
    name="Product 1",
    image="https://example.com/product.jpg",
    price=99.99,
    quantiles=10,
)

print("\n=============================\n")
print(product.model_dump())
print("\n=============================\n")
print(product.model_dump_json())
print("\n=============================\n")
