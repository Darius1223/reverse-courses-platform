import enum
from typing import Optional

from sqlmodel import Field, SQLModel


class UserTypes(str, enum.Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"


class UserBase(SQLModel):
    firstname: str
    lastname: str
    surname: str

    email: str

    hashed_password: str

    telephone: str

    role: UserTypes


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class UserUpdate(UserBase):
    pass
