from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    user_id: int
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr

class Item(BaseModel):
    item_id: int
    name: str
    description: str | None = None

class NumRequest(BaseModel):
    num: int