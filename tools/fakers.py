from faker import Faker
from datetime import datetime
class Fake:

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def pet_name(self) -> str:
        return self.faker.first_name()

    def status(self) -> str:
        return self.faker.random_element(["available", "pending", "sold"])

    def photo_url(self) -> str:
        return self.faker.image_url()

    def category_name(self) -> str:
        return self.faker.random_element(["dog", "cat", "bird"])

    def tag_name(self) -> str:
        return self.faker.word()

    def id(self) -> int:
        return self.faker.random_int(min=1, max=10000)

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def quantity(self) -> int:
        return self.faker.random_int(min=1, max=10)

    def ship_date(self) -> datetime:
        return self.faker.date_time()

    def status_store(self) -> str:
        return self.faker.random_element(["placed", "approved", "delivered"])

    def complete(self) -> bool:
        return self.faker.boolean()


fake = Fake(faker=Faker())