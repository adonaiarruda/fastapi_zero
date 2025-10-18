# fastapi_zero.schemas
from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    # message: Annotated[str, Field(min_length=3, max_length=100)]
    # message: int


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
