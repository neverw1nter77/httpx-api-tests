import allure
from httpx import Request, Response

from tools.logger import get_logger
from tools.curl import make_curl_from_request

logger = get_logger(__name__)


def curl_event_hook(request: Request):
    """
    Attaches a cURL representation of the HTTP request to the Allure report.

    :param request: The outgoing HTTP request.
    """
    curl_command = make_curl_from_request(request)
    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    Logs information about the outgoing HTTP request.

    :param request: The outgoing HTTP request.
    """
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    """
    Logs information about the received HTTP response.

    :param response: The incoming HTTP response.
    """
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )