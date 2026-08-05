import allure
from pages.base_page import BasePage
from locators.main_page_lct import MainPageLocators
from locators.auth_page_lct import AuthPageLocators
from locators.feed_page_lct import FeedPageLocators


class MainPage(BasePage):
    
    
    @allure.step('Клик на кнопку "Личный кабинет" на главной странице')
    def click_on_lc_button_base_page(self):
        
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Переход в профиль')
    def go_to_profile(self):
        
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на кнопку "Конструктор"')
    def click_on_constructor_button(self):
        
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_on_orders_list_button(self):
        
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик на первый ингредиент')
    def click_on_ingredient(self):
        
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Закрыть модальное окно ингредиента')
    def click_on_close_ingredient_window(self):
        
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        
        return self.driver.current_url

    @allure.step('Ожидание открытия модального окна с деталями ингредиента')
    def wait_window_details_ingredients(self):
        
        return self.check_element_displayed(MainPageLocators.MODAL_DETAILS)

    @allure.step('Проверка отображения заголовка конструктора')
    def check_constructor_title_displayed(self):
        
        return self.check_element_displayed(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Проверка отображения заголовка ленты заказов')
    def check_feed_title_displayed(self):
        
        return self.check_element_displayed(FeedPageLocators.FEED_TITLE)

    @allure.step('Проверка отображения заголовка деталей ингредиента')
    def check_modal_details_title_displayed(self):
        
        return self.check_element_displayed(MainPageLocators.MODAL_DETAILS)

    @allure.step('Проверка что модальное окно закрыто')
    def check_window_exit(self):
        
        return not self.check_element_displayed(MainPageLocators.MODAL_DETAILS)

    @allure.step('Получение значения счетчика ингредиента')
    def get_ingredient_counter(self):
        
        element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return element.text

    @allure.step('Drag-and-drop ингредиента в конструктор')
    def drag_and_drop_ingredient(self):
        
        self.drag_and_drop_on_element(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_SECTION
        )

    @allure.step('Проверка активности кнопки "Оформить заказ"')
    def check_order_button_enabled(self):
        
        return self.is_element_enabled(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_create_order_button(self):
        
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверка отображения модального окна с подтверждением заказа')
    def check_order_submitted_modal_displayed(self):
        
        return self.check_element_displayed(MainPageLocators.ORDER_SUBMITTED_MODAL)

    @allure.step('Проверка что кнопка "Личный кабинет" отображается')
    def check_profile_button_displayed(self):
        
        return self.check_element_displayed(MainPageLocators.PROFILE_BUTTON)