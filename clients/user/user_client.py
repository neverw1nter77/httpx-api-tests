import allure

from clients.api_client import APIClient
from httpx import Response
from clients.http_builder import get_http_client
from tools.routes import APIRoutes
from clients.user.user_schema import (CreateUserRequestSchema, CreateUserResponseSchema, UpdateUserRequestSchema,
                                      LoginRequestSchema)

class UserClient(APIClient):

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Creates a new user.

        :param request: Request body with user data.
        :return: Raw HTTP response.
        """
        return self.post(APIRoutes.USER, json=request.model_dump(by_alias=True))

    @allure.step("Update user: {username}")
    def update_user_api(self, request: UpdateUserRequestSchema, username: str) -> Response:
        """
        Updates an existing user.

        :param request: Request body with updated user data.
        :param username: Username of the user to update.
        :return: Raw HTTP response.
        """
        return self.put(f"{APIRoutes.USER}/{username}", json=request.model_dump(by_alias=True))

    @allure.step("Get user: {username}")
    def get_user_api(self, username: str) -> Response:
        """
        Retrieves a user by username.

        :param username: Username.
        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.USER}/{username}")

    @allure.step("Delete user: {username}")
    def delete_user_api(self, username: str) -> Response:
        """
        Deletes a user by username.

        :param username: Username.
        :return: Raw HTTP response.
        """
        return self.delete(f"{APIRoutes.USER}/{username}")

    @allure.step("Login user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Logs in a user.

        :param request: Login request data.
        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.USER}/login", params=request.model_dump())

    @allure.step("Logout user")
    def logout_api(self) -> Response:
        """
        Logs out the current user.

        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.USER}/logout")

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_user_client() -> UserClient:
    """
    Creates a UserClient instance with a configured HTTP client.

    :return: UserClient instance.
    """
    return UserClient(client=get_http_client())