from faker import Faker
import random
import string
from typing import Dict, Optional, List

fake = Faker()


class DataGenerator:
    
    @staticmethod
    def generate_user_data() -> Dict[str, str]:
        
        return {
            "email": fake.email(),
            "password": fake.password(length=8),
            "name": fake.first_name()
        }
    
    @staticmethod
    def generate_user_without_field(field_to_remove: str) -> Dict[str, str]:

        user_data = DataGenerator.generate_user_data()
        if field_to_remove in user_data:
            del user_data[field_to_remove]
        return user_data
    
    @staticmethod
    def generate_invalid_password() -> str:
        return fake.password(length=2)  
    
    @staticmethod
    def generate_invalid_email() -> str:
        return f"{fake.first_name()}_at_{fake.domain_name()}"
    
    @staticmethod
    def generate_random_ingredients(count: int = 2) -> List[str]:
       

        available_ingredients = [
            "60d3b41abdacab0026a733c6",
            "61c0c5a71d1f82001bdaaa6f",
            "60d3b41abdacab0026a733c7",
            "60d3b41abdacab0026a733c8",
            "60d3b41abdacab0026a733c9"
        ]
        return random.sample(available_ingredients, min(count, len(available_ingredients)))
    
    @staticmethod
    def generate_unique_email() -> str:
        """Сгенерировать уникальный email с timestamp."""
        timestamp = int(fake.date_time().timestamp())
        return f"test_user_{timestamp}@example.com"
    
    @staticmethod
    def generate_strong_password(length: int = 12) -> str:
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def generate_order_data(ingredients: Optional[List[str]] = None) -> Dict:
        
        if ingredients is None:
            ingredients = DataGenerator.generate_random_ingredients()
        
        return {
            "ingredients": ingredients
        }
    
    @staticmethod
    def generate_order_without_ingredients() -> Dict:

        return {
            "ingredients": []
        }