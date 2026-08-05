import allure
import pytest
from pages.main_page import MainPage
from config import BASE_URL


class TestMainPage:

    @allure.title("Проверка перехода по нажатию кнопки 'Личный кабинет'")
    @allure.description("Проверка, что при клике на кнопку 'Личный кабинет' происходит переход на страницу авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_on_lc_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_lc_button_base_page()
        current_url = main_page.get_current_url()
        assert "login" in current_url.lower() or "auth" in current_url.lower(), \
            f"Ожидался переход на страницу логина, получен URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Конструктор'")
    @allure.description("Проверка, что при клике на кнопку 'Конструктор' происходит переход на главную страницу")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_lc_button_base_page()
        main_page.click_on_constructor_button()
        current_url = main_page.get_current_url()
        assert BASE_URL in current_url, f"Ожидался {BASE_URL}, получен {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу 'Лента заказов'")
    @allure.description("Проверка, что при клике на 'Лента заказов' происходит переход на страницу с заказами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_feed_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_orders_list_button()
        current_url = main_page.get_current_url()
        assert "feed" in current_url.lower() or "orders" in current_url.lower(), \
            f"Ожидался переход на страницу заказов, получен URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка клика по ингредиенту и открытие модального окна")
    @allure.description("Проверка, что при клике на ингредиент открывается модальное окно с деталями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_on_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_ingredient()
        assert main_page.wait_window_details_ingredients(), \
            "Модальное окно с деталями ингредиента не открылось"
        allure.attach("Модальное окно с деталями ингредиента открыто", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка закрытия модального окна ингредиента")
    @allure.description("Проверка, что модальное окно закрывается при клике на крестик")
    @allure.severity(allure.severity_level.NORMAL)
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_on_ingredient()
        assert main_page.wait_window_details_ingredients(), "Модальное окно не открылось"
        main_page.click_on_close_ingredient_window()
        assert main_page.check_window_exit() is False, "Модальное окно не закрылось"
        allure.attach("Модальное окно закрыто", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка увеличения счетчика ингредиента")
    @allure.description("Проверка, что при добавлении ингредиента в конструктор увеличивается счетчик")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        initial_count = main_page.get_ingredient_counter()
        allure.attach(f"Начальный счетчик: {initial_count}", 
                     name="Данные", 
                     attachment_type=allure.attachment_type.TEXT)
        main_page.drag_and_drop_ingredient()
        new_count = main_page.get_ingredient_counter()
        allure.attach(f"Новый счетчик: {new_count}", 
                     name="Данные", 
                     attachment_type=allure.attachment_type.TEXT)
        assert int(new_count) > int(initial_count), \
            f"Счетчик не увеличился. Было: {initial_count}, Стало: {new_count}"
        allure.attach(f"Счетчик успешно увеличен до {new_count}", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)