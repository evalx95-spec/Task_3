import allure
import pytest
from pages.profile_page import ProfilePage
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from config import BASE_URL
from data import TestData


class TestProfilePage:
    """Тесты для страницы профиля."""

    @allure.title("Переход в историю заказов")
    @allure.description("Проверка перехода на страницу истории заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_orders_history(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_page()
        auth_page.login_as_existing_user()
        main_page.go_to_profile()
        profile_page.click_orders_history_button()
        current_url = profile_page.get_current_url()
        assert "orders" in current_url.lower() or "history" in current_url.lower(), \
            f"Ожидался переход на страницу истории заказов, получен URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта по кнопке 'Выйти'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_logout(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_page()
        auth_page.login_as_existing_user()
        main_page.go_to_profile()
        profile_page.click_logout_button()
        assert auth_page.check_login_page_opened(), \
            "Страница логина не открылась после выхода"
        current_url = profile_page.get_current_url()
        assert "login" in current_url.lower() or "auth" in current_url.lower(), \
            f"Ожидался переход на страницу логина, получен URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Получение URL профиля")
    @allure.description("Проверка получения URL страницы профиля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_profile_url(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_page()
        auth_page.login_as_existing_user()
        main_page.go_to_profile()
        current_url = profile_page.get_profile_url()
        assert "profile" in current_url.lower(), \
            f"Ожидался URL страницы профиля, получен: {current_url}"
        allure.attach(current_url, name="URL профиля", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Получение URL истории заказов")
    @allure.description("Проверка получения URL страницы истории заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_orders_history_url(self, driver):
        main_page = MainPage(driver)
        auth_page = AuthPage(driver)
        profile_page = ProfilePage(driver)
        main_page.open_page()
        auth_page.login_as_existing_user()
        main_page.go_to_profile()
        profile_page.click_orders_history_button()
        current_url = profile_page.get_orders_history_url()
        assert "orders" in current_url.lower() or "history" in current_url.lower(), \
            f"Ожидался URL страницы истории заказов, получен: {current_url}"
        allure.attach(current_url, name="URL истории заказов", attachment_type=allure.attachment_type.TEXT)