# Pydantic Hindi - Complete Learning Guide

## 📚 Project Overview
Comprehensive Pydantic learning project with hands-on examples and assignments.

## 🏗️ Project Structure
```
01-foundation/          # Basic Pydantic models
02-fields-validation/   # Field validation & constraints  
03-model-behavior/      # Validators & computed fields
04-nested-models/       # Complex nested structures
05-serialization/       # Data serialization/deserialization
fastapi/               # FastAPI integration
```

## 🎯 Learning Path

### 1. Foundation
**Basic BaseModel usage, type annotations, data validation**
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool
```

### 2. Fields & Validation
**Field constraints, optional fields, descriptions**
```python
from pydantic import BaseModel, Field

class Employee(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    salary: float = Field(..., ge=10000)
```

### 3. Model Behavior
**Custom validators, computed fields**
```python
@field_validator('username')
def username_length(cls, v):
    if len(v) < 4:
        raise ValueError("Username must be at least 4 characters")
    return v

@computed_field
@property
def total_price(self) -> float:
    return self.price * self.quantity
```

### 4. Nested Models
**Embedding models, self-referencing**
```python
class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address  # Nested model
```

### 5. Serialization
**Data conversion, JSON encoding**
```python
model.model_dump()          # → dict
model.model_dump_json()     # → JSON string
Model.model_validate(data)  # Create from dict
```

### 6. FastAPI Integration
**Request/Response models, dependency injection**
```python
@app.post('/signup')
def signup(user: UserSignup):
    return {'message': f'User {user.username} signed up'}
```

## 🚀 Quick Start
```bash
pip install -e .
python 01-foundation/examples/first_model.py
```

## 📝 Key Concepts Cheatsheet

### Field Validation
```python
field: str = Field(min_length=3, max_length=50)
number: int = Field(ge=0, le=100)
```

### Validators
```python
@field_validator('field_name')
@model_validator(mode='after')
```

### Common Patterns
```python
# Optional with default
field: Optional[str] = None

# Collections
items: List[str]
mapping: Dict[str, int]

# Custom validation
@field_validator('email')
def validate_email(cls, v):
    if '@' not in v:
        raise ValueError('Invalid email')
    return v
```

## 🎯 Practice Tips
1. Start with basic models, add complexity gradually
2. Use Field constraints for data integrity
3. Test with invalid data to understand validation
4. Leverage Python's type system fully
5. Read Pydantic's detailed validation errors