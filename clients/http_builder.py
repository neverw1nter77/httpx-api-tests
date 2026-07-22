from httpx import Client
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook


def get_http_client() -> Client:
    """
    Создаёт базовый HTTP клиент.

    :return: httpx.Client
    """
    return Client(
        base_url="https://petstore.swagger.io/v2",
        timeout=100,
        event_hooks={
            "request": [
                curl_event_hook,
                log_request_event_hook
            ],
            "response": [
                log_response_event_hook
            ],
        }
    )