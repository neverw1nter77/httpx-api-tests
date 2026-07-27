from pydantic import BaseModel, Field, ConfigDict
from tools.fakers import fake


class CategorySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str

class TagSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    name: str

class PetSchema(BaseModel):
    """
    Represents the Pet entity structure.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int
    category: CategorySchema
    name: str
    photo_urls: list[str] = Field(alias="photoUrls")
    tags: list[TagSchema]
    status: str

class CreatePetRequestSchema(BaseModel):
    """
    Schema for creating a new pet.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(id=fake.id(), name=fake.category_name()))
    name: str = Field(default_factory=fake.pet_name)
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=lambda: [fake.photo_url()])
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(id=fake.id(), name=fake.tag_name())])
    status: str = Field(default_factory=fake.status)

class CreatePetResponseSchema(PetSchema):
    """
    Schema for pet creation response.
    """
    pass

class UpdatePetRequestSchema(BaseModel):
    """
    Schema for updating a pet.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(default_factory=fake.id)
    category: CategorySchema = Field(default_factory=lambda: CategorySchema(id=fake.id(), name=fake.category_name()))
    name: str = Field(default_factory=fake.pet_name)
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=lambda: [fake.photo_url()])
    tags: list[TagSchema] = Field(default_factory=lambda: [TagSchema(id=fake.id(), name=fake.tag_name())])
    status: str = Field(default_factory=fake.status)

class UpdatePetResponseSchema(PetSchema):
    """
    Schema for pet update response.
    """
    pass