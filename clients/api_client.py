from typing import Any
import allure
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

class APIClient:
    def __init__(self, client: Client):
        """
        Base API client for HTTP requests.
        Provides logging, basic error handling, and Allure steps.
        """
        self.client = client

    @allure.step("GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Sends a GET request.

        :param url: Endpoint URL.
        :param params: Query parameters (e.g., ?key=value).
        :return: Response object containing the server response.
        """
        return self.client.get(url, params=params)

    @allure.step("POST request to {url}")
    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Sends a POST request.

        :param url: Endpoint URL.
        :param json: Data in JSON format.
        :param data: Form data (e.g., application/x-www-form-urlencoded).
        :param files: Files to upload.
        :return: Response object containing the server response.
        """
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("PUT request to {url}")
    def put(
            self,
            url: URL | str,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
    ) -> Response:
        """
        Sends a PUT request (full update of a resource).

        :param url: Endpoint URL.
        :param json: Data for updating in JSON format.
        :return: Response object containing the server response.
        """
        return self.client.put(url, json=json, data=data, files=files)

    @allure.step("DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        Sends a DELETE request (removes a resource).

        :param url: Endpoint URL.
        :return: Response object containing the server response.
        """
        return self.client.delete(url)