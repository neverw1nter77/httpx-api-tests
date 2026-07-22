import allure

from clients.api_client import APIClient
from httpx import Response
from clients.http_builder import get_http_client
from tools.routes import APIRoutes
from clients.user.user_schema import (CreateUserRequestSchema, CreateUserResponseSchema, UpdateUserRequestSchema,
                                      UpdateUserResponseSchema, LoginRequestSchema)

class UserClient(APIClient):

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание юзера.

        :param request: Тело запроса с данными юзера
        :return: Ответ от сервера (httpx.Response)
        """
        return self.post(APIRoutes.USER, json=request.model_dump(by_alias=True))

    @allure.step("Update user: {username}")
    def update_user_api(self, request: UpdateUserRequestSchema, username: str) -> Response:
        """
        Обновление юзера.

        :param request: Тело запроса с данными юзера
        :return: Ответ от сервера (httpx.Response)
        """
        return self.put(f"{APIRoutes.USER}/{username}", json=request.model_dump(by_alias=True))

    @allure.step("Get user: {username}")
    def get_user_api(self, username: str) -> Response:
        """
        Получение юзера по username.

        :param username: имя юзера
        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.USER}/{username}")

    @allure.step("Delete user: {username}")
    def delete_user_api(self, username: str) -> Response:
        """
        Удаление юзера по username.

        :param username: имя юзера
        :return: Ответ от сервера (httpx.Response)
        """
        return self.delete(f"{APIRoutes.USER}/{username}")

    @allure.step("Login user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.get(
            f"{APIRoutes.USER}/login",
            params=request.model_dump()
        )

    @allure.step("Logout user")
    def logout_api(self) -> Response:
        """
        Разлогин юзера

        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.USER}/logout")

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_user_client() -> UserClient:
    """
    Создаёт UserClient с базовым HTTP клиентом.

    :return: UserClient
    """
    return UserClient(client=get_http_client())