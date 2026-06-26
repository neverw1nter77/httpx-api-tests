from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class CategorySchema(BaseModel):
    # Позволяет передавать данные как по имени поля (snake_case), так и по его alias (camelCase).
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str

class TagSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str

class PetSchema(BaseModel):
    """
        Описание структуры Pet.
        """
    model_config = ConfigDict(populate_by_name=True)

    id: int
    category: CategorySchema
    name: str
    photo_urls: list[str] = Field(alias="photoUrls")
    tags: list[TagSchema]
    status: str

class CreatePetRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(id=fake.id(), name=fake.category_name()))
    name: str = Field(default_factory=fake.pet_name)
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=lambda: [fake.photo_url()])
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(id=fake.id(), name=fake.tag_name())])
    status: str = Field(default_factory=fake.status)

class CreatePetResponseSchema(PetSchema):
    pass

class UpdatePetRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(id=fake.id(), name=fake.category_name()))
    name: str = Field(default_factory=fake.pet_name)
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=lambda: [fake.photo_url()])
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(id=fake.id(), name=fake.tag_name())])
    status: str = Field(default_factory=fake.status)

class UpdatePetResponseSchema(PetSchema):
    pass