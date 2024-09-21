from pydantic import BaseModel, Field


class UserCreateRequestl(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    username: str = Field(max_length=8)
    email: str = Field(max_length=255)
    password: str = Field(max_length=16)