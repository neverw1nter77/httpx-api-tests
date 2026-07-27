from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Represents the user entity structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int
    username: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    password: str
    phone: str
    user_status: int = Field(alias="userStatus")

class UserApiResponse(BaseModel):
    """
    Base schema for user-related API responses.
    """
    code: int
    type: str
    message: str

class CreateUserRequestSchema(BaseModel):
    """
    Schema for creating a new user.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    username: str = Field(default_factory=fake.user_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    email: str = Field(default_factory=fake.user_email)
    password: str = Field(default_factory=fake.user_password)
    phone: str = Field(default_factory=fake.user_phone)
    user_status: int = Field(alias="userStatus", default_factory=fake.user_status)

class CreateUserResponseSchema(UserApiResponse):
    """
    Schema for user creation response.
    """
    pass

class UpdateUserRequestSchema(BaseModel):
    """
    Schema for updating a user.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    username: str = Field(default_factory=fake.user_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    email: str = Field(default_factory=fake.user_email)
    password: str = Field(default_factory=fake.user_password)
    phone: str = Field(default_factory=fake.user_phone)
    user_status: int = Field(alias="userStatus", default_factory=fake.user_status)

class UpdateUserResponseSchema(UserApiResponse):
    """
    Schema for user update response.
    """
    pass

class LoginRequestSchema(BaseModel):
    """
    Schema for user login request.
    """
    username: str
    password: str


class LoginResponseSchema(BaseModel):
    """
    Schema for user login response.
    """
    code: int
    type: str
    message: str
