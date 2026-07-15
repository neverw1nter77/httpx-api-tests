from http import HTTPStatus

import pytest
from assertions.base import assert_status_code
from assertions.user_assertions import assert_create_user_response, assert_get_user_response, \
    assert_update_user_response, assert_login_user_response
from fixtures.user_fixture import UserFixture, UserClient
from clients.user.user_schema import (CreateUserResponseSchema, CreateUserRequestSchema,
                                      UpdateUserRequestSchema, UpdateUserResponseSchema,
                                      LoginResponseSchema, LoginRequestSchema)

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

    def test_update_user(self, user_client: UserClient, function_user: UserFixture):
        request = UpdateUserRequestSchema(
            id=function_user.request.id,
            username=function_user.request.username,
            firstName=function_user.request.first_name,
            lastName=function_user.request.last_name,
            email="example@test.com",
            password="123456",
            phone=function_user.request.phone,
            userStatus=function_user.request.user_status
        )
        response = user_client.update_user_api(
            request,
            function_user.request.username
        )
        response_data = UpdateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_user_response(request, response_data)
        get_response = user_client.get_user_api(request.username)
        get_data = CreateUserRequestSchema.model_validate_json(get_response.text)

        assert_get_user_response(request, get_data)

    def test_delete_user(self, user_client: UserClient, function_user: UserFixture):
        username = function_user.request.username
        response = user_client.delete_user_api(username)
        assert_status_code(response.status_code, HTTPStatus.OK)
        get_response = user_client.get_user_api(username)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

    def test_login_user(self, user_client: UserClient, function_user: UserFixture):
        request = LoginRequestSchema(
            username=function_user.request.username,
            password=function_user.request.password
        )
        response = user_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_user_response(response_data)

    def test_logout(self, user_client: UserClient):
        response = user_client.logout_api()
        assert_status_code(response.status_code, HTTPStatus.OK)


