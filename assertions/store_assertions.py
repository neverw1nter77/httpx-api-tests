from assertions.base import assert_equal
from clients.store.store_schema import CreateOrderRequestSchema, CreateOrderResponseSchema

def assert_create_order_response(
        request: CreateOrderRequestSchema,
        response: CreateOrderResponseSchema):
    """
    Verifies that the created order matches the request data.
    """
    assert response.id is not None
    assert_equal(response.status, request.status, "status")
    assert_equal(response.petId, request.petId, "petId")
    assert_equal(response.quantity, request.quantity, "quantity")
    assert_equal(response.complete, request.complete, "complete")

def assert_get_order_response(
        request: CreateOrderRequestSchema,
        response: CreateOrderResponseSchema):
    """
    Verifies that the retrieved order matches the request data.
    """
    assert_equal(response.id, request.id, "id")
    assert_equal(response.status, request.status, "status")
    assert_equal(response.petId, request.petId, "petId")
    assert_equal(response.quantity, request.quantity, "quantity")
    assert_equal(response.complete, request.complete, "complete")