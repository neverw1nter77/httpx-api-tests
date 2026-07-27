from enum import Enum

class AllureStory(str, Enum):
    """
    Enum containing Allure story names.
    """
    CREATE = "Create entity"
    GET = "Get entity"
    UPDATE = "Update entity"
    DELETE = "Delete entity"
    NEGATIVE = "Negative scenarios"
    AUTH = "Authentication"