from typing import Annotated

from fastapi import Form


class RegistrationsRequestForm:
    def __init__(
        self,
        *,
        email: Annotated[
            str,
            Form(),
        ],
        firstname: Annotated[
            str,
            Form(),
        ],
        lastname: Annotated[
            str,
            Form(),
        ],
        surname: Annotated[
            str,
            Form(),
        ],
        telephone: Annotated[
            str,
            Form(),
        ],
        role: Annotated[
            str,
            Form(),
        ],
    ):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.surname = surname
        self.telephone = telephone
        self.role = role
