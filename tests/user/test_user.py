from http import HTTPStatus

import pytest
from assertions.base import assert_status_code
from assertions.user_assertions import assert_create_user_response, assert_get_user_response
from fixtures.user_fixture import UserFixture, UserClient
from clients.user.user_schema import CreateUserResponseSchema, CreateUserRequestSchema

@pytest.mark.regression
@pytest.mark.user
class TestUser:

    def test_create_user(self, user_client: UserClient):
        request = CreateUserRequestSchema()
        response = user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

    def test_get_user(self, user_client: UserClient, function_user: UserFixture):
        username = function_user.request.username
        response = user_client.get_user_api(username)
        response_data = CreateUserRequestSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(function_user.request, response_data)




