import pytest
from pydantic import BaseModel

from clients.pet.pet_client import get_pet_client, PetClient
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema
class PetFixture(BaseModel):
    request: CreatePetRequestSchema
    response: CreatePetResponseSchema

@pytest.fixture
def pet_client() -> PetClient:
    # Создаем готовый апи клиент
    return get_pet_client()

@pytest.fixture
def function_pet(pet_client: PetClient):
    request = CreatePetRequestSchema()
    response = pet_client.create_pet_api(request)
    response_data = CreatePetResponseSchema.model_validate_json(response.text)

    return PetFixture(
        request=request,
        response=response_data
    )

