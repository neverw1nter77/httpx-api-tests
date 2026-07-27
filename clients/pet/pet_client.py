from clients.api_client import APIClient
import allure
from typing import BinaryIO
from httpx import Response
from clients.pet.pet_schema import CreatePetRequestSchema, CreatePetResponseSchema, UpdatePetRequestSchema
from tools.routes import APIRoutes
from clients.http_builder import get_http_client


class PetClient(APIClient):
    @allure.step("Create pet")
    def create_pet_api(self, request: CreatePetRequestSchema) -> Response:
        """
        Creates a new pet.

        :param request: Request body with pet data.
        :return: Raw HTTP response.
        """
        return self.post(APIRoutes.PET, json=request.model_dump(by_alias=True))

    @allure.step("Update pet (PUT)")
    def update_pet_api(self, request: UpdatePetRequestSchema) -> Response:
        """
        Fully updates a pet.

        :param request: Request body with updated pet data.
        :return: Raw HTTP response.
        """
        return self.put(APIRoutes.PET, json=request.model_dump(by_alias=True))

    @allure.step("Get pet by id: {pet_id}")
    def get_pet_by_id_api(self, pet_id: int) -> Response:
        """
        Retrieves a pet by its ID.

        :param pet_id: Pet ID.
        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.PET}/{pet_id}")

    @allure.step("Get pets by status: {status}")
    def get_pet_by_status_api(self, status: str) -> Response:
        """
        Retrieves a list of pets filtered by status.

        :param status: Pet status (available, pending, sold).
        :return: Raw HTTP response.
        """
        return self.get(f"{APIRoutes.PET}/findByStatus", params={"status": status})

    @allure.step("Upload image for pet {pet_id}")
    def upload_image_api(self, pet_id: int, file: BinaryIO) -> Response:
        """
        Uploads an image for a pet.

        :param pet_id: Pet ID.
        :param file: Image file (binary stream).
        :return: Raw HTTP response.
        """
        return self.post(f"{APIRoutes.PET}/{pet_id}/uploadImage", files={"file": file})

    @allure.step("Delete pet {pet_id}")
    def delete_pet_api(self, pet_id: int) -> Response:
        """
        Deletes a pet.

        :param pet_id: Pet ID.
        :return: Raw HTTP response.
        """
        return self.delete(f"{APIRoutes.PET}/{pet_id}")

    @allure.step("Update pet by id {pet_id}")
    def update_pet_by_id_api(self, pet_id: int, name: str, status: str) -> Response:
        """
        Partially updates pet fields (name and status).

        :param pet_id: Pet ID.
        :param name: New pet name.
        :param status: New pet status.
        :return: Raw HTTP response.
        """
        return self.post(f"{APIRoutes.PET}/{pet_id}", data={"name": name, "status": status})

    def create_pet(self, request: CreatePetRequestSchema) -> CreatePetResponseSchema:
        response = self.create_pet_api(request)
        return CreatePetResponseSchema.model_validate_json(response.text)

def get_pet_client() -> PetClient:
    """
    Creates a PetClient instance with a configured HTTP client.

    :return: PetClient instance.
    """
    return PetClient(client=get_http_client())
