from enum import Enum

class AllureStory(str, Enum):
    CREATE = "Create entity"
    GET = "Get entity"
    UPDATE = "Update entity"
    DELETE = "Delete entity"
    NEGATIVE = "Negative scenarios"
    AUTH = "Authentication"