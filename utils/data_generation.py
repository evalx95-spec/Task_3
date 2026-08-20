import allure
from faker import Faker

fake = Faker("ru_RU")

def generate_user_payload():
    with allure.step(
            f'Сгенерить рандомные креды пользователя'):
        return {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.user_name()
        }