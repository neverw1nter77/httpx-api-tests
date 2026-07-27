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
        Creates a new order.

        :param request: Request body with order data.
        :return: Raw HTTP response.
        """
        return self.post(f"{APIRoutes.STORE}/order", json=request.model_dump(by_alias=True, mode="json"))

    @allure.step("Get order by id: {order_id}")
    def get_order_by_id_api(self, order_id: int) -> Response:
        """
        Retrieves an order by its ID.

        :param order_id: Order ID.
        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.STORE}/order/{order_id}")

    @allure.step("Get store inventory")
    def get_store_inventory_api(self) -> Response:
        """
        Retrieves store inventory.

        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.STORE}/inventory")

    @allure.step("Delete order by id: {order_id}")
    def delete_order_by_id_api(self, order_id: int) -> Response:
        """
        Deletes an order by its ID.

        :param order_id: Order ID.
        :return: Raw HTTP response.
        """
        return self.delete(f"{APIRoutes.STORE}/order/{order_id}")

    def create_order(self, request: CreateOrderRequestSchema) -> CreateOrderResponseSchema:
        response = self.create_order_api(request)
        return CreateOrderResponseSchema.model_validate_json(response.text)

def get_order_client() -> OrderClient:
    """
    Creates an OrderClient instance with a configured HTTP client.

    :return: OrderClient instance.
    """
    return OrderClient(client=get_http_client())
