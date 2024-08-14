import enum

from pydantic import BaseModel, Field


class UserEnum(str, enum.Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"


class UserSchema(BaseModel):
    id_: int = Field(alias="id")
    role: UserEnum
