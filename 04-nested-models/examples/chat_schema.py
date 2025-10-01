from pydantic import BaseModel, Field
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    profile_image: Optional[str] = None
    email: Optional[str] = None
    is_active: bool = Field(default=True)


class Chat(BaseModel):
    id: int
    user: User
    content: str
    replies: Optional[List["Chat"]] = []


Chat.model_rebuild()

user = User(
    id=1,
    name="Hitesh",
    profile_image="https://example.com/profile.jpg",
    email="hitesh@example.com",
    is_active=True,
)

chat = Chat(
    id=1,
    user=user,
    content="Hello, world!",
)
chat.replies.extend(
    [
        Chat(
            id=2,
            user=user,
            content="Reply 1",
        ),
        Chat(
            id=3,
            user=user,
            content="Reply 2",
        ),
    ]
)
print(chat.model_dump())
