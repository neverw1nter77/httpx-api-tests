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
        Создание пит омца.

        :param request: Тело запроса с данными питомца
        :return: Ответ от сервера (httpx.Response)
        """
        return self.post(APIRoutes.PET, json=request.model_dump(by_alias=True))

    @allure.step("Update pet (PUT)")
    def update_pet_api(self, request: UpdatePetRequestSchema) -> Response:
        """
        Полное обновление питомца.

        :param request: Тело запроса с обновлёнными данными питомца
        :return: Ответ от сервера (httpx.Response)
        """
        return self.put(APIRoutes.PET, json=request.model_dump(by_alias=True))

    @allure.step("Get pet by id: {pet_id}")
    def get_pet_by_id_api(self, pet_id: int) -> Response:
        """
        Получение питомца по ID.

        :param pet_id: ID питомца
        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.PET}/{pet_id}")

    @allure.step("Get pets by status: {status}")
    def get_pet_by_status_api(self, status: str) -> Response:
        """
        Получение списка питомцев по статусу.

        :param status: Статус питомца (available, pending, sold)
        :return: Ответ от сервера (httpx.Response)
        """
        return self.get(f"{APIRoutes.PET}/findByStatus", params={"status": status})

    @allure.step("Upload image for pet {pet_id}")
    def upload_image_api(self, pet_id: int, file: BinaryIO) -> Response:
        """
        Загрузка изображения для питомца.

        :param pet_id: ID питомца
        :param file: Файл изображения (binary)
        :return: Ответ от сервера (httpx.Response)
        """
        return self.post(f"{APIRoutes.PET}/{pet_id}/uploadImage", files={"file": file})

    @allure.step("Delete pet {pet_id}")
    def delete_pet_api(self, pet_id: int) -> Response:
        """
        Удаление питомца.

        :param pet_id: ID питомца
        :return: Ответ от сервера (httpx.Response)
        """
        return self.delete(f"{APIRoutes.PET}/{pet_id}")

    @allure.step("Update pet by id {pet_id}")
    def update_pet_by_id_api(self, pet_id: int, name: str, status: str) -> Response:
        """
        Частичное обновление питомца (имя и статус).

        :param pet_id: ID питомца
        :param name: Новое имя питомца
        :param status: Новый статус питомца
        :return: Ответ от сервера (httpx.Response)
        """
        return self.post(f"{APIRoutes.PET}/{pet_id}", data={"name": name, "status": status})

    def create_pet(self, request: CreatePetRequestSchema) -> CreatePetResponseSchema:
        response = self.create_pet_api(request)
        return CreatePetResponseSchema.model_validate_json(response.text)

def get_pet_client() -> PetClient:
    """
    Создаёт PetClient с базовым HTTP клиентом.

    :return: PetClient
    """
    return PetClient(client=get_http_client())
