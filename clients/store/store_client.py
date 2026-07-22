import allure

from clients.api_client import APIClient
from httpx import Response
from clients.store.store_schema import CreateOrderResponseSchema, CreateOrderRequestSchema
from clients.http_builder import get_http_client
from tools.routes import APIRoutes
class OrderClient(APIClient):

    @allure.step("Create order")
    def create_order_api(self, request: CreateOrderRequestSchema) -> Response:
        """
        Создание заказа.

        :param request: Тело запроса с данными заказа
        :return: Ответ от сервера (httpx.Response)
        """
        return self.post(f"{APIRoutes.STORE}/order", json=request.model_dump(by_alias=True, mode="json"))

    @allure.step("Get order by id: {order_id}")
    def get_order_by_id_api(self, order_id: int) -> Response:
        """
        Получение заказа по ID.

        :param order_id: ID заказа
        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.STORE}/order/{order_id}")

    @allure.step("Get store inventory")
    def get_store_inventory_api(self) -> Response:
        """
        Получение списка инвенторя.

        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.STORE}/inventory")

    @allure.step("Delete order by id: {order_id}")
    def delete_order_by_id_api(self, order_id: int) -> Response:
        """
        Удаление заказа.

        :param order_id: ID заказа
        :return: Ответ от сервера (httpx.Response)
        """
        return self.delete(f"{APIRoutes.STORE}/order/{order_id}")

    def create_order(self, request: CreateOrderRequestSchema) -> CreateOrderResponseSchema:
        response = self.create_order_api(request)
        return CreateOrderResponseSchema.model_validate_json(response.text)

def get_order_client() -> OrderClient:
    """
    Создаёт OrderClient с базовым HTTP клиентом.

    :return: OrderClient
    """
    return OrderClient(client=get_http_client())
