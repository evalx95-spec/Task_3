import allure
import pytest
from pages.base_page import BasePage
from config import BASE_URL, ENDPOINTS


class TestBasePage:
    
    @allure.title("Проверка перехода по нажатию кнопки 'Личный кабинет'")
    @allure.description("Проверка, что при клике на кнопку 'Личный кабинет' происходит переход на страницу авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_on_lc_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page()
        
        assert base_page.check_element_displayed(BasePage.PROFILE_BUTTON_LOCATOR), \
            "Кнопка 'Личный кабинет' не отображается на странице"
        
        base_page.click_on_element(BasePage.PROFILE_BUTTON_LOCATOR)
        
        current_url = base_page.get_current_url()
        
        assert "login" in current_url.lower() or "auth" in current_url.lower(), \
            f"Ожидался переход на страницу логина, получен URL: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Конструктор'")
    @allure.description("Проверка, что при клике на кнопку 'Конструктор' происходит переход на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_constructor_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page()
        
        assert base_page.check_element_displayed(BasePage.CONSTRUCTOR_BUTTON_LOCATOR), \
            "Кнопка 'Конструктор' не отображается на странице"
        
        base_page.click_on_element(BasePage.CONSTRUCTOR_BUTTON_LOCATOR)
        
        current_url = base_page.get_current_url()
        
        assert BASE_URL in current_url, f"Ожидался {BASE_URL}, получен {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Лента заказов'")
    @allure.description("Проверка, что при клике на 'Лента заказов' происходит переход на страницу с заказами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_feed_button(self, driver):
        base_page = BasePage(driver)
        base_page.open_page()
        
        assert base_page.check_element_displayed(BasePage.FEED_BUTTON_LOCATOR), \
            "Кнопка 'Лента заказов' не отображается на странице"
        
        base_page.click_on_element(BasePage.FEED_BUTTON_LOCATOR)
        
        current_url = base_page.get_current_url()
        
        assert "feed" in current_url.lower() or "orders" in current_url.lower(), \
            f"Ожидался переход на страницу заказов, получен URL: {current_url}"
        
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)