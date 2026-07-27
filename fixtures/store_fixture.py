import pytest
from pydantic import BaseModel
from clients.store.store_client import get_order_client, OrderClient
from clients.store.store_schema import CreateOrderResponseSchema, CreateOrderRequestSchema

class OrderFixture(BaseModel):
    """
    Combines request and response data for an order entity.
    """
    request: CreateOrderRequestSchema
    response: CreateOrderResponseSchema

@pytest.fixture()
def order_client() -> OrderClient:
    """
    Provides an OrderClient instance.

    :return: OrderClient
    """
    return get_order_client()

@pytest.fixture()
def function_order(order_client: OrderClient):
    """
    Creates an order and returns both request and response data.

    :param order_client: OrderClient instance.
    :return: OrderFixture containing request and response.
    """
    request = CreateOrderRequestSchema()
    response = order_client.create_order(request)

    return OrderFixture(
        request=request,
        response=response
    )