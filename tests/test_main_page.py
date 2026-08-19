import allure
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPage:

    @allure.title("Проверка перехода на страницу сбора бургера по нажатию на 'Конструктор'")
    @allure.description("При клике на кнопку 'Конструктор' должен открыться конструктор бургера и отображаться заголовок 'Соберите бургер'.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_constructor_button()
        assert main_page.is_constructor_title_displayed(), "Заголовок 'Соберите бургер' не отображается"
        allure.attach("Заголовок конструктора успешно найден", name="Результат проверки", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка перехода на страницу со всеми заказами по нажатию на 'Лента заказов'")
    @allure.description("При клике на 'Лента заказов' должен открыться фид заказов, URL должен содержать '/feed'.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_orders_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_feed_button()
        current_url = main_page.get_current_url()
        assert "/feed" in current_url, f"URL не содержит '/feed', текущий URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка клика по ингредиенту и появление всплывающего окна 'Детали ингредиентов'")
    @allure.description("Клик по ингредиенту должен открывать модальное окно с заголовком 'Детали ингредиента'.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_ingredient_and_get_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_displayed(), "Модальное окно 'Детали ингредиента' не открылось"
        allure.attach("Модальное окно успешно открыто", name="Результат проверки", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка закрытия окна 'Детали ингредиентов' по нажатию на крестик")
    @allure.description("После клика на крестик модальное окно должно закрыться и больше не отображаться.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_displayed(), "Модальное окно не открылось перед проверкой закрытия"
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed(), "Модальное окно не закрылось после клика на крестик"
        allure.attach("Модальное окно успешно закрыто", name="Результат проверки", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Проверка добавления ингредиента в конструктор через drag-and-drop")
    @allure.description("Перетаскивание ингредиента в область конструктора должно добавить его в корзину; в корзине должен быть хотя бы один элемент.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()

        main_page.clear_constructor_basket()
        allure.attach("Корзина приведена в чистое состояние (localStorage очищен, страница обновлена)", name="Статус корзины", attachment_type=allure.attachment_type.TEXT)

        
        main_page.drag_ingredient_to_constructor()
        allure.attach("Выполнен drag-and-drop ингредиента в область конструктора", name="Действие", attachment_type=allure.attachment_type.TEXT)

        
        main_page.wait_for_ingredient_in_basket()

        
        assert main_page.is_ingredient_in_basket(), "Ингредиент не отображается в корзине после drag-and-drop"
        allure.attach("Ингредиент успешно добавлен в корзину конструктора", name="Результат", attachment_type=allure.attachment_type.TEXT)
