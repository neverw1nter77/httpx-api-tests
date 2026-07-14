import pytest
from pydantic import BaseModel
from clients.user.user_schema import CreateUserResponseSchema, CreateUserRequestSchema
from clients.user.user_client import UserClient, get_user_client

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

@pytest.fixture
def user_client() -> UserClient:
    return get_user_client()

@pytest.fixture
def function_user(user_client: UserClient):
    request = CreateUserRequestSchema()
    response = user_client.create_user(request)

    return UserFixture(
        request=request,
        response=response
    )
