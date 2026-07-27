from pydantic import BaseModel


class HTTPClientSettings(BaseModel):
    """
    Configuration for the HTTP client.
    """
    client_url: str = "https://petstore.swagger.io/v2"
    timeout: int = 10


class Settings(BaseModel):
    """
    Application settings container.
    """
    http_client: HTTPClientSettings = HTTPClientSettings()


settings = Settings()