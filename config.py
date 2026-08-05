import os
from pathlib import Path


BASE_URL = "https://qa-stellarburgers.education-services.ru"
BASE_API_URL = "https://qa-stellarburgers.education-services.ru"


ENDPOINTS = {
   
    'CREATE_USER': '/api/auth/register',
    'LOGIN_USER': '/api/auth/login',
    'UPDATE_USER': '/api/auth/user',
    'DELETE_USER': '/api/auth/user',
    'LOGOUT_USER': '/api/auth/logout',
    
    # Заказы
    'CREATE_ORDER': '/api/orders',
    'GET_USER_ORDERS': '/api/orders',
    'GET_INGREDIENTS': '/api/ingredients',
}


DEFAULT_TIMEOUT = 10
IMPLICIT_WAIT = 5
PAGE_LOAD_TIMEOUT = 30


BROWSER = "chrome"
HEADLESS = False
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


ROOT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
ALLURE_RESULTS_DIR = ROOT_DIR / "allure-results"
REPORTS_DIR = ROOT_DIR / "reports"