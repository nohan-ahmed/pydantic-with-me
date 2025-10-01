from pydantic import BaseModel
from typing import List, Optional

from starlette.responses import Content


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address


class Comment(BaseModel):
    id: int
    content: str
    # NOTE: It is called forward reference, 
    replies: Optional[List["Comment"]] = None

# we need to call model_rebuild() after defining the nested model
Comment.model_rebuild()

address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="10001",
)

user = User(
    id=1,
    name="Hitesh",
    address=address,
)


comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2"),
        Comment(id=4, content="reply3", replies=[
            Comment(id=5, content="reply4"),
        ]),
    ],
)

print(comment.model_dump())
