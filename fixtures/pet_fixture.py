import pytest
from pydantic import BaseModel

from clients.pet.pet_client import get_pet_client, PetClient
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema

class PetFixture(BaseModel):
    """
    Combines request and response data for a pet entity.
    """
    request: CreatePetRequestSchema
    response: CreatePetResponseSchema

@pytest.fixture
def pet_client() -> PetClient:
    """
    Provides a PetClient instance.

    :return: PetClient
    """
    return get_pet_client()

@pytest.fixture
def function_pet(pet_client: PetClient):
    """
    Creates a pet and returns both request and response data.

    :param pet_client: PetClient instance.
    :return: PetFixture containing request and response.
    """
    request = CreatePetRequestSchema()
    response = pet_client.create_pet(request)

    return PetFixture(
        request=request,
        response=response
    )

