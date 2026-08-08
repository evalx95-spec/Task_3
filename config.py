# config.py
"""Конфигурационные настройки тестового окружения."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# === ВРЕМЕННЫЕ НАСТРОЙКИ ===

DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 10))
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', 5))
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', 30))

# === НАСТРОЙКИ БРАУЗЕРА ===

BROWSER = os.getenv('BROWSER', 'chrome')
HEADLESS = os.getenv('HEADLESS', 'False').lower() == 'true'
WINDOW_WIDTH = int(os.getenv('WINDOW_WIDTH', 1920))
WINDOW_HEIGHT = int(os.getenv('WINDOW_HEIGHT', 1080))

# === ПУТИ К ФАЙЛАМ ===

ROOT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
ALLURE_RESULTS_DIR = ROOT_DIR / "allure-results"
REPORTS_DIR = ROOT_DIR / "reports"

# === ТЕСТОВЫЕ ДАННЫЕ ===

class TestCredentials:
    """Тестовые учетные данные."""
    
    EXISTING_USER = {
        'email': os.getenv('EXISTING_USER_EMAIL', 'test@example.com'),
        'password': os.getenv('EXISTING_USER_PASSWORD', 'password123'),
        'name': os.getenv('EXISTING_USER_NAME', 'Test User')
    }
    
    NEW_USER = {
        'email': os.getenv('NEW_USER_EMAIL', 'newuser@example.com'),
        'password': os.getenv('NEW_USER_PASSWORD', 'newpassword123'),
        'name': os.getenv('NEW_USER_NAME', 'New User')
    }
    
    @classmethod
    def get_existing_user(cls):
        """Получить данные существующего пользователя."""
        return cls.EXISTING_USER
    
    @classmethod
    def get_new_user(cls):
        """Получить данные нового пользователя."""
        return cls.NEW_USER