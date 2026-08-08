import allure  
import pytest
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from utils.urls import BASE_URL, Urls
from data import TestData


class TestProfilePage:
    
    @allure.title("Переход в профиль через кнопку 'Личный кабинет'")
    @allure.description("Проверка перехода в профиль авторизованного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_go_to_profile(self, driver):
        """Проверка, что авторизованный пользователь может перейти в профиль."""
        main_page = MainPage(driver)
        main_page.open_page()
        
        main_page.click_profile_button()
        
        auth_page = AuthPage(driver)
        auth_page.login_as_existing_user()
     
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), \
            "Страница профиля не открылась"
        
        current_url = profile_page.get_current_url()
        assert Urls.PROFILE in current_url, \
            f"Ожидался URL профиля, получен: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта через кнопку 'Выход'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self, driver):
        """Проверка, что пользователь может выйти из аккаунта."""
        main_page = MainPage(driver)
        main_page.open_page()
        
       
        main_page.click_profile_button()
        
        auth_page = AuthPage(driver)
        auth_page.login_as_existing_user()
        
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), \
            "Страница профиля не открылась"
        
        profile_page.click_logout_button()
        
        assert auth_page.is_login_button_displayed(), \
            "Кнопка 'Войти' не отображается после выхода"
        
        current_url = auth_page.get_current_url()
        assert Urls.LOGIN in current_url, \
            f"Ожидался переход на страницу логина, получен: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка отображения данных пользователя в профиле")
    @allure.description("Проверка, что в профиле отображаются данные авторизованного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_profile_data_displayed(self, driver):
        """Проверка отображения данных пользователя в профиле."""
        main_page = MainPage(driver)
        main_page.open_page()
        
        main_page.click_profile_button()
        
        auth_page = AuthPage(driver)
        auth_page.login_as_existing_user()
        
    
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), \
            "Страница профиля не открылась"
        
        
        user_email = profile_page.get_user_email()
        
        
        allure.attach(f"Email из профиля: {user_email}", 
                      name="Email пользователя", 
                      attachment_type=allure.attachment_type.TEXT)
        
    
        assert user_email != "", "Email пользователя не должен быть пустым"
        assert "@" in user_email, f"Email '{user_email}' должен содержать '@'"
        
        
        assert user_email == TestData.EXISTING_USER['email'], \
            f"Email '{user_email}' не соответствует ожидаемому '{TestData.EXISTING_USER['email']}'"

    @allure.title("Переход в конструктор из профиля")
    @allure.description("Проверка перехода в конструктор из профиля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_constructor_from_profile(self, driver):
        """Проверка, что из профиля можно перейти в конструктор."""
        main_page = MainPage(driver)
        main_page.open_page()
        
        
        main_page.click_profile_button()
        
        
        auth_page = AuthPage(driver)
        auth_page.login_as_existing_user()
        
        
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), \
            "Страница профиля не открылась"
        
        
        main_page.click_constructor_button()
        
        current_url = main_page.get_current_url()
        assert BASE_URL in current_url or Urls.HOME in current_url, \
            f"Ожидался переход на главную страницу, получен: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Переход в историю заказов из профиля")
    @allure.description("Проверка перехода в историю заказов из профиля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_order_history_from_profile(self, driver):
        """Проверка, что из профиля можно перейти в историю заказов."""
        main_page = MainPage(driver)
        main_page.open_page()
        
        
        main_page.click_profile_button()
        
        auth_page = AuthPage(driver)
        auth_page.login_as_existing_user()
        
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_opened(), \
            "Страница профиля не открылась"
        
        profile_page.click_order_history_button()
        
        assert profile_page.is_order_history_page_opened(), \
            "Страница истории заказов не открылась"
        
        current_url = profile_page.get_current_url()
        assert Urls.ORDERS_HISTORY in current_url, \
            f"Ожидался URL истории заказов, получен: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)