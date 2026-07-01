from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    username: str = Field(nullable=False)
    email: str = Field(unique=True)
    