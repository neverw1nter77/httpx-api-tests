import pytest
from pydantic import BaseModel
from clients.store.store_client import get_order_client, OrderClient
from clients.store.store_schema import CreateOrderResponseSchema, CreateOrderRequestSchema

class OrderFixture(BaseModel):
    request: CreateOrderRequestSchema
    response: CreateOrderResponseSchema

@pytest.fixture()
def order_client() -> OrderClient:
    # Создаем готовый апи клиент
    return get_order_client()

@pytest.fixture()
def function_order(order_client: OrderClient):
    request = CreateOrderRequestSchema()
    response = order_client.create_order(request)

    return OrderFixture(
        request=request,
        response=response
    )