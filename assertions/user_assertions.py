from assertions.base import assert_equal
from clients.user.user_schema import CreateUserRequestSchema


def assert_create_user_response(request, response):
    assert_equal(response.code, 200, "code")
    assert_equal(response.type, "unknown", "type")
    assert_equal(response.message, str(request.id), "message")

def assert_get_user_response(
    request: CreateUserRequestSchema,
    response: CreateUserRequestSchema
):
    assert_equal(response.id, request.id, "id")
    assert_equal(response.username, request.username, "username")
    assert_equal(response.first_name, request.first_name, "first_name")
    assert_equal(response.last_name, request.last_name, "last_name")
    assert_equal(response.email, request.email, "email")
    assert_equal(response.phone, request.phone, "phone")
    assert_equal(response.user_status, request.user_status, "user_status")
