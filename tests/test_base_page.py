import allure
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from utils.urls import BASE_URL, Urls  


class TestMainPageNavigation:

    @allure.title("Проверка перехода по нажатию кнопки 'Личный кабинет'")
    @allure.description("Проверка, что при клике на кнопку 'Личный кабинет' происходит переход на страницу авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_on_lc_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        assert main_page.is_profile_button_displayed(), \
            "Кнопка 'Личный кабинет' не отображается на странице"
        
        main_page.click_profile_button()
        
        auth_page = AuthPage(driver)
        current_url = auth_page.get_current_url()
        
        assert Urls.LOGIN in current_url.lower(), \
            f"Ожидался переход на страницу логина, получен URL: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Конструктор'")
    @allure.description("Проверка, что при клике на кнопку 'Конструктор' происходит переход на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        assert main_page.is_constructor_button_displayed(), \
            "Кнопка 'Конструктор' не отображается на странице"
        
        main_page.click_constructor_button()
        
        current_url = main_page.get_current_url()
        
        assert BASE_URL in current_url, f"Ожидался {BASE_URL}, получен {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Лента заказов'")
    @allure.description("Проверка, что при клике на 'Лента заказов' происходит переход на страницу с заказами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        
        assert main_page.is_feed_button_displayed(), \
            "Кнопка 'Лента заказов' не отображается на странице"
        
        main_page.click_feed_button()
        
        current_url = main_page.get_current_url()
        
        assert Urls.FEED in current_url.lower(), \
            f"Ожидался переход на страницу заказов, получен URL: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)