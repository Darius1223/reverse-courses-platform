import enum

from pydantic import BaseModel, Field, ConfigDict


class UserEnum(str, enum.Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_: int = Field(alias="id")
    role: UserEnum
