# conftest.py
import pytest
import allure
import sys
import os
from pathlib import Path

# Добавляем корневую директорию в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Импорт для автоматического управления драйверами (рекомендуется)
try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.edge.service import Service as EdgeService
    WEBDRIVER_MANAGER_AVAILABLE = True
except ImportError:
    WEBDRIVER_MANAGER_AVAILABLE = False
    print("WebDriver Manager not installed. Install it with: pip install webdriver-manager")

# Импорт из utils
from utils.urls import BASE_URL
from config import BROWSER, HEADLESS, WINDOW_WIDTH, WINDOW_HEIGHT, DEFAULT_TIMEOUT
from helpers import DataGenerator
from data import TestData


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и закрытия драйвера.
    
    Использует WebDriver Manager если установлен, иначе стандартный подход.
    """
    driver = None
    
    if BROWSER.lower() == "chrome":
        options = Options()
        if HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        # Оптимизация для тестов
        options.add_argument("--log-level=3")  # Только критические ошибки
        
        if WEBDRIVER_MANAGER_AVAILABLE:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            driver = webdriver.Chrome(options=options)
    
    elif BROWSER.lower() == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument(f"--width={WINDOW_WIDTH}")
        options.add_argument(f"--height={WINDOW_HEIGHT}")
        
        if WEBDRIVER_MANAGER_AVAILABLE:
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            driver = webdriver.Firefox(options=options)
    
    elif BROWSER.lower() == "edge":
        options = EdgeOptions()
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
        
        if WEBDRIVER_MANAGER_AVAILABLE:
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        else:
            driver = webdriver.Edge(options=options)
    
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    
    
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    driver.maximize_window()
    
    yield driver
    
    
    driver.quit()


@pytest.fixture(scope="function")
def driver_with_screenshot_on_failure(driver, request):
   
    yield driver
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"screenshot_{request.node.name}",
            attachment_type=allure.attachment_type.PNG
        )
       
        screenshots_dir = Path(__file__).parent / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)
        screenshot_path = screenshots_dir / f"{request.node.name}_{int(driver.get_current_url().timestamp())}.png"
        driver.save_screenshot(str(screenshot_path))


@pytest.fixture
def base_url():
    """Фикстура с базовым URL."""
    return BASE_URL


@pytest.fixture
def existing_user():
    """Фикстура с данными существующего пользователя."""
    return TestData.EXISTING_USER


@pytest.fixture
def new_user_data():
    """Фикстура с данными нового пользователя."""
    return DataGenerator.generate_user_data()


@pytest.fixture
def invalid_credentials():
    """Фикстура с невалидными данными для входа."""
    return TestData.INVALID_CREDENTIALS


@pytest.fixture
def invalid_login_cases():
    """Фикстура с набором невалидных данных для входа."""
    return TestData.INVALID_LOGIN_CASES


@pytest.fixture
def default_ingredients():
    """Фикстура с ингредиентами по умолчанию."""
    return TestData.DEFAULT_INGREDIENTS


@pytest.fixture
def error_messages():
    """Фикстура с сообщениями об ошибках."""
    return TestData.ERROR_MESSAGES


@pytest.fixture
def expected_urls():
    """Фикстура с ожидаемыми URL."""
    return TestData.EXPECTED_URLS


@pytest.fixture(autouse=True)
def add_allure_environment(request):
    """Добавление информации об окружении в Allure."""
    allure.attach(
        f"Browser: {BROWSER}\n"
        f"Headless: {HEADLESS}\n"
        f"Base URL: {BASE_URL}\n"
        f"Timeout: {DEFAULT_TIMEOUT}",
        name="Environment",
        attachment_type=allure.attachment_type.TEXT
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
   
    setattr(item, "rep_" + rep.when, rep)
    
    if rep.when == "call" and rep.failed:
        
        if "driver" in item.fixturenames:
            driver = item.funcargs.get("driver")
            if driver:
                try:
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=f"screenshot_{item.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as e:
                    print(f"Failed to take screenshot: {e}")
        
        
        if rep.longrepr:
            allure.attach(
                str(rep.longrepr),
                name="Error details",
                attachment_type=allure.attachment_type.TEXT
            )


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Настройка тестового окружения перед запуском всех тестов."""
    
    screenshots_dir = Path(__file__).parent / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)
    
    allure_results_dir = Path(__file__).parent / "allure-results"
    allure_results_dir.mkdir(exist_ok=True)
    
    print(f"\n=== Test Environment Setup ===")
    print(f"Browser: {BROWSER}")
    print(f"Headless: {HEADLESS}")
    print(f"Base URL: {BASE_URL}")
    print(f"Screenshots dir: {screenshots_dir}")
    print("===============================\n")
    
    yield
    
    print("\n=== Test Environment Cleanup ===")
    print("All tests completed")
    print("================================\n")



@pytest.fixture(scope="session")
def session_driver():
    """
    Фикстура для использования одного драйвера на всю сессию.
    Используется с осторожностью, т.к. тесты должны быть независимы.
    """
    options = Options()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    if WEBDRIVER_MANAGER_AVAILABLE:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()