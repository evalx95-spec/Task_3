import sys
from pathlib import Path


project_root = str(Path(__file__).resolve().parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service


from utils.urls import BASE_URL
from config import BROWSER, HEADLESS, WINDOW_WIDTH, WINDOW_HEIGHT, DEFAULT_TIMEOUT
from helpers import DataGenerator


@pytest.fixture(scope="function")
def driver():
    driver = None

    if BROWSER.lower() == "chrome":
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--log-level=3")

        service = Service()
        driver = webdriver.Chrome(service=service, options=options)

    elif BROWSER.lower() == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument(f"--width={WINDOW_WIDTH}")
        options.add_argument(f"--height={WINDOW_HEIGHT}")

        service = Service()
        driver = webdriver.Firefox(service=service, options=options)

    elif BROWSER.lower() == "edge":
        options = EdgeOptions()
        if HEADLESS:
            options.add_argument("--headless")
        options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")

        service = Service()
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    driver.implicitly_wait(DEFAULT_TIMEOUT)

    yield driver
    driver.quit()


@pytest.fixture
def new_user_data():
    return DataGenerator.generate_user_data()


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

                    screenshots_dir = Path(__file__).parent / "screenshots"
                    screenshots_dir.mkdir(exist_ok=True)
                    screenshot_path = screenshots_dir / f"{item.name}_{rep.when}.png"
                    driver.save_screenshot(str(screenshot_path))
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
    screenshots_dir = Path(__file__).parent / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    allure_results_dir = Path(__file__).parent / "allure-results"
    allure_results_dir.mkdir(exist_ok=True)

    print("\n=== Test Environment Setup ===")
    print(f"Browser: {BROWSER}")
    print(f"Headless: {HEADLESS}")
    print(f"Base URL: {BASE_URL}")
    print(f"Screenshots dir: {screenshots_dir}")
    print("===============================\n")

    yield

    print("\n=== Test Environment Cleanup ===")
    print("All tests completed")
    print("================================\n")

