from httpx import Client
from config import settings


def get_http_client() -> Client:
    """
    Создаёт базовый HTTP клиент.

    :return: httpx.Client
    """
    return Client(
        base_url=settings.http_client.client_url,
        timeout=settings.http_client.timeout,
    )