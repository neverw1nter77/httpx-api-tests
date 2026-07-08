from http import HTTPStatus

import pytest

from assertions.base import assert_status_code
from assertions.pet_assertions import assert_create_pet_response, assert_get_pet_response, assert_update_pet_response, \
    assert_get_pet_by_status_response
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

    def test_delete_pet(self, function_pet: PetFixture, pet_client: PetClient):
        pet_id = function_pet.response.id
        response = pet_client.delete_pet_api(pet_id)
        assert_status_code(response.status_code, HTTPStatus.OK)
        get_response = pet_client.get_pet_by_id_api(pet_id)
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)

    def test_get_pet_by_status(self, function_pet: PetFixture, pet_client: PetClient):
        pet_status = function_pet.response.status
        response = pet_client.get_pet_by_status_api(pet_status)

        assert_status_code(response.status_code, HTTPStatus.OK)

        response_data = []
        for item in response.json():
            try:
                pet = CreatePetResponseSchema.model_validate(item)
                response_data.append(pet)
            except Exception:
                continue

        assert_get_pet_by_status_response(function_pet.response, response_data)

    def test_create_pet_negative(self, pet_client: PetClient):
        request = {
            "name": " ",
            "photoUrls": "None"
        }

        response = pet_client.post("/pet", json=request)

        assert response.status_code in [
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.INTERNAL_SERVER_ERROR
        ]

        response_data = response.json()
        print(response_data)

        assert "code" in response_data
        assert "message" in response_data



    def test_get_pet_not_found(self, pet_client: PetClient):
        invalid_pet_id = 999999999

        response = pet_client.get_pet_by_id_api(invalid_pet_id)

        print("STATUS:", response.status_code)
        print("BODY:", response.text)

        assert response.status_code == HTTPStatus.NOT_FOUND

        data = response.json()
        assert data["message"] == "Pet not found"