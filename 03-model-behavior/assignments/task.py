from pydantic import BaseModel, field_validator, model_validator, computed_field, Field # type: ignore

# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights : int= Field(..., gt=1)
    rate_per_night: float = Field(...)
    password: str
    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value
    confirm_password: str
    @field_validator('confirm_password')
    def validate_confirm_password(cls, value):
        if len(value) < 8: 
            raise ValueError("Confirm password must be at least 8 characters long")
        return value

    @model_validator(mode='after')
    def validate_password_match(cls, fields_value):
        if fields_value.password != fields_value.confirm_password:
            raise ValueError("Password and confirm password do not match")
        return fields_value

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_night

book = Booking(
    user_id=1,
    room_id=101,
    nights=3,
    rate_per_night=100.0,
    password='123456780',
    confirm_password='123456780'
)

print(book)
