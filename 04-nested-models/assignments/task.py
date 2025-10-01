from optparse import Option
from pydantic import BaseModel #type: ignore
from typing import List, Optional

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Course(BaseModel):
    id: int
    name: str
    modules: Optional[List['Module']] = []

class Module(BaseModel):
    id: int
    name :str
    lessons : Optional[List[Lesson]] = None

class Lesson(BaseModel):
    id: int
    name: str