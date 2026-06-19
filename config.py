from pydantic import BaseModel


class HTTPClientSettings(BaseModel):
    client_url: str = "https://petstore.swagger.io/v2"
    timeout: int = 10


class Settings(BaseModel):
    http_client: HTTPClientSettings = HTTPClientSettings()


settings = Settings()