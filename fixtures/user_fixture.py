import pytest
from pydantic import BaseModel
from clients.user.user_schema import CreateUserResponseSchema, CreateUserRequestSchema
from clients.user.user_client import UserClient, get_user_client

class UserFixture(BaseModel):
    """
    Combines request and response data for a user entity.
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

@pytest.fixture
def user_client() -> UserClient:
    """
    Provides a UserClient instance.

    :return: UserClient
    """
    return get_user_client()

@pytest.fixture
def function_user(user_client: UserClient):
    """
    Creates a user and returns both request and response data.

    :param user_client: UserClient instance.
    :return: UserFixture containing request and response.
    """
    request = CreateUserRequestSchema()
    response = user_client.create_user(request)

    return UserFixture(
        request=request,
        response=response
    )
