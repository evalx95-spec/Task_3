import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import BASE_URL  # Импортируем из config


def pytest_addoption(parser):
    
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser option: chrome or firefox"
    )


@pytest.fixture()
def driver(request):
    
    browser_name = request.config.getoption("--browser")
    
    if browser_name.lower() == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        
    elif browser_name.lower() == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
        
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    
    driver.implicitly_wait(5)
    
    
    driver.get(BASE_URL)
    
    yield driver
    
    
    driver.quit()


@pytest.fixture
def base_page(driver):
    
    from pages.base_page import BasePage
    return BasePage(driver)


@pytest.fixture
def main_page(driver):
    
    from pages.main_page import MainPage
    return MainPage(driver)


@pytest.fixture
def auth_page(driver):
    
    from pages.auth_page import AuthPage
    return AuthPage(driver)