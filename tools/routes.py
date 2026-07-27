from enum import Enum


class APIRoutes(str, Enum):
    """
    Enum containing base API routes.
    """
    PET = "/pet"
    STORE = "/store"
    USER = "/user"


    def __str__(self):
        return self.value