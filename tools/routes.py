from enum import Enum


class APIRoutes(str, Enum):
    PET = "/pet"
    STORE = "/store"
    USER = "/user"


    def __str__(self):
        return self.value