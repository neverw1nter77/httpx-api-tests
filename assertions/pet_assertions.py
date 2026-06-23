from assertions.base import assert_status_code, assert_equal
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema

def assert_create_pet_response(
        request: CreatePetRequestSchema,
        response: CreatePetResponseSchema):
    assert response.id is not None
    assert_equal(response.name, request.name, "name")
    assert_equal(response.status, request.status, "status")
