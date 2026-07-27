from enum import Enum

class AllureFeature(str, Enum):
    """
    Enum containing Allure feature names.
    """
    PET = "Pet"
    USER = "User"
    STORE = "Store"