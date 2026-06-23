from http import HTTPStatus

import pytest

from assertions.base import assert_status_code
from assertions.pet_assertions import assert_create_pet_response
from fixtures.pet_fixture import PetFixture, PetClient
from clients.pet.pet_schema import CreatePetRequestSchema,CreatePetResponseSchema

def test_create_pet(pet_client: PetClient):
    request = CreatePetRequestSchema()
    print(request)
    response = pet_client.create_pet_api(request)
    response_data = CreatePetResponseSchema.model_validate_json(response.text)
    print(response_data)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_pet_response(request, response_data)

