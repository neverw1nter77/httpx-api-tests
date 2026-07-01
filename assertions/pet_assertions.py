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

def assert_get_pet_by_status_response(expected_pet, response_list):
    assert len(response_list) > 0, "Response list is empty"
    pet = next((item for item in response_list if item.id == expected_pet.id), None)
    assert pet is not None, f"Pet with id {expected_pet.id} not found in response"

    assert_equal(pet.id, expected_pet.id, "id")
    assert_equal(pet.name, expected_pet.name, "name")
    assert_equal(pet.status, expected_pet.status, "status")

