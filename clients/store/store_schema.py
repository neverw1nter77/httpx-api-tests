from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake
from datetime import datetime


class OrderSchema(BaseModel):
    """модель ДАННЫХ (как объект выглядит)"""
    model_config = ConfigDict(populate_by_name=True)

    id: int
    petId: int
    quantity: int
    ship_date: datetime = Field(alias="shipDate")
    status: str
    complete: bool

class CreateOrderRequestSchema(BaseModel):
    """модель ЗАПРОСА (что я отправляю)"""
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    petId: int = Field(default_factory=fake.id)
    quantity: int = Field(default_factory=fake.quantity)
    ship_date: datetime = Field(alias="shipDate", default_factory=fake.ship_date)
    status: str = Field(default_factory=fake.status_store)
    complete: bool = Field(default_factory=fake.complete)

class CreateOrderResponseSchema(OrderSchema):
    pass