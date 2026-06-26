from assertions.base import assert_status_code, assert_equal
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema, UpdatePetRequestSchema


def assert_create_pet_response(
        request: CreatePetRequestSchema,
        response: CreatePetResponseSchema):
    assert response.id is not None
    assert_equal(response.name, request.name, "name")
    assert_equal(response.status, request.status, "status")


def assert_get_pet_response(
        request: CreatePetRequestSchema,
        response: CreatePetResponseSchema):
    assert_equal(response.id, request.id, "id")
    assert_equal(response.name, request.name, "name")
    assert_equal(response.status, request.status, "status")

def assert_update_pet_response(
        request: UpdatePetRequestSchema,
        response: CreatePetResponseSchema):

    assert_equal(response.id, request.id, "id")
    assert_equal(response.name, request.name, "name")
    assert_equal(response.status, request.status, "status")
