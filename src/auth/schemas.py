from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: str = Field(max_length=255)
    password: str = Field(max_length=16)