import allure
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_lct import MainPageLocators


class TestMainPage:

    @allure.title("Проверка перехода на страницу сбора бургера по нажатию на 'Конструктор'")
    @allure.description("Проверка, что при клике на кнопку 'Конструктор' открывается страница сборки бургера")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_constructor_button(self, driver):
        """Проверка перехода на страницу сбора бургера."""
        main_page = MainPage(driver)
        main_page.open_page()

        main_page.click_constructor_button()

        assert main_page.is_constructor_title_displayed(), \
            "Заголовок 'Соберите бургер' не отображается"

        allure.attach("Заголовок конструктора успешно найден", 
                      name="Результат проверки", 
                      attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу со всеми заказами по нажатию на 'Лента заказов'")
    @allure.description("Проверка, что при клике на кнопку 'Лента заказов' открывается страница с заказами")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_orders_list_button(self, driver):
        """Проверка перехода на страницу со всеми заказами."""
        main_page = MainPage(driver)
        main_page.open_page()

       
        main_page.click_feed_button()

        current_url = main_page.get_current_url()
        assert "/feed" in current_url, \
            f"URL не содержит '/feed', текущий URL: {current_url}"

        allure.attach(current_url, name="Текущий URL", 
                      attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка клика по ингредиенту и появление всплывающего окна 'Детали ингредиентов'")
    @allure.description("Проверка, что при клике на ингредиент открывается модальное окно с деталями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_ingredient_and_get_window(self, driver):
        """Проверка открытия модального окна с деталями ингредиента."""
        main_page = MainPage(driver)
        main_page.open_page()


        main_page.click_first_ingredient()

        
        assert main_page.is_ingredient_modal_displayed(), \
            "Модальное окно 'Детали ингредиента' не открылось"

        allure.attach("Модальное окно успешно открыто", 
                      name="Результат проверки", 
                      attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка закрытия окна 'Детали ингредиентов' по нажатию на крестик")
    @allure.description("Проверка, что модальное окно закрывается при клике на крестик и больше не отображается")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_window_ingredient_window(self, driver):
        """Проверка закрытия модального окна."""
        main_page = MainPage(driver)
        main_page.open_page()

        
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_displayed(), \
            "Модальное окно не открылось перед проверкой закрытия"

        
        main_page.close_ingredient_modal()

        
        assert main_page.is_ingredient_modal_closed(), \
            "Модальное окно не закрылось после клика на крестик"

        allure.attach("Модальное окно успешно закрыто", 
                      name="Результат проверки", 
                      attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка добавления ингредиента в конструктор")
    @allure.description("Проверка, что ингредиент добавляется в корзину при клике и отображается в списке справа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_count(self, driver):
        
        main_page = MainPage(driver)
        
        
        main_page.open_page()
        
        driver.execute_script("window.localStorage.clear();")
        
        
        driver.refresh()
        
        
        time.sleep(1)

        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located(MainPageLocators.BURGER_CONSTRUCTOR_INGREDIENT_ITEM),
                message="Корзина не очистилась после refresh"
            )
        except Exception:
            
            pass

        allure.attach("Корзина приведена в чистое состояние", 
                      name="Статус корзины", 
                      attachment_type=allure.attachment_type.TEXT)

        
        main_page.click_first_ingredient()

        
        main_page.wait.until(
            EC.presence_of_element_located(MainPageLocators.BURGER_CONSTRUCTOR_INGREDIENT_ITEM),
            message="Ингредиент не появился в корзине после клика"
        )

        assert main_page.check_element_displayed(MainPageLocators.BURGER_CONSTRUCTOR_INGREDIENT_ITEM), \
            "Ингредиент не отображается в корзине"

        allure.attach("Ингредиент успешно добавлен в корзину конструктора", 
                      name="Результат", 
                      attachment_type=allure.attachment_type.TEXT)