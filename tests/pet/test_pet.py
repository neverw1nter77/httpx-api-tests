from http import HTTPStatus

import pytest

from assertions.base import assert_status_code
from assertions.pet_assertions import assert_create_pet_response, assert_get_pet_response, assert_update_pet_response
from fixtures.pet_fixture import PetFixture, PetClient
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema, UpdatePetRequestSchema

@pytest.mark.regression
@pytest.mark.pet
class TestPet:

    def test_create_pet(self, pet_client: PetClient):
        request = CreatePetRequestSchema()
        response = pet_client.create_pet_api(request)
        response_data = CreatePetResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_pet_response(request, response_data)


    def test_get_pet(self, function_pet: PetFixture, pet_client: PetClient):
        pet_id = function_pet.response.id
        response = pet_client.get_pet_by_id_api(pet_id)
        response_data = CreatePetResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_pet_response(function_pet.request, response_data)


    def test_update_pet(self, function_pet: PetFixture, pet_client: PetClient):
        request = UpdatePetRequestSchema(
            id=function_pet.response.id,
            name="BarsikTest",
            category=function_pet.response.category,
            photoUrls=function_pet.response.photo_urls,
            tags=function_pet.response.tags,
            status=function_pet.response.status
        )

        response = pet_client.update_pet_api(request)
        response_data = CreatePetResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_pet_response(request, response_data)



