from sqlmodel import Field, SQLModel
from typing import Optional

class User(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(unique=True)

class Item(SQLModel, table=True):
    item_id: int = Field(primary_key=True)
    name: str
    description: Optional[str] = None
    price: float

class NodeBase(SQLModel):
    value: int

class Node(NodeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
