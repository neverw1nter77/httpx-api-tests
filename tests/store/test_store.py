from http import HTTPStatus

import pytest
from assertions.base import assert_status_code
from fixtures.store_fixture import OrderFixture, OrderClient
from clients.store.store_schema import CreateOrderRequestSchema, CreateOrderResponseSchema
from assertions.store_assertions import assert_create_order_response, assert_get_order_response
@pytest.mark.regression
@pytest.mark.store
class TestOrder:

    def test_create_order(self, order_client: OrderClient):
        request = CreateOrderRequestSchema()
        response = order_client.create_order_api(request)
        response_data = CreateOrderResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_order_response(request, response_data)

    def test_get_order(self, function_order: OrderFixture, order_client: OrderClient):
        order_id = function_order.response.id
        response = order_client.get_order_by_id_api(order_id)
        response_data = CreateOrderResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_order_response(function_order.request, response_data)

    def test_delete_order(self, function_order: OrderFixture, order_client: OrderClient):
        order_id = function_order.response.id
        response = order_client.delete_order_by_id_api(order_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        get_response = order_client.get_order_by_id_api(order_id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

    def test_create_order_negative(self, order_client: OrderClient):
        request = {
            "petId": "invalid",
            "status": "wrong_status"
        }

        response = order_client.post("/store/order", json=request)

        assert response.status_code in [
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.INTERNAL_SERVER_ERROR
        ]

        data = response.json()

        assert "code" in data
        assert "message" in data

    def test_get_order_not_found(self, order_client: OrderClient):
        invalid_order_id = -1

        response = order_client.get_order_by_id_api(invalid_order_id)

        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

        data = response.json()
        assert data["message"] == "Order not found"