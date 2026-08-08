import allure
from pages.base_page import BasePage
from locators.main_page_lct import MainPageLocators


class MainPage(BasePage):
    
    
    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_profile_button(self):
        """Переход в личный кабинет"""
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor_button(self):
        """Переход в конструктор"""
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_feed_button(self):
        """Переход в ленту заказов"""
        self.click_on_element(MainPageLocators.FEED_BUTTON)
        self.wait_for_page_load()

    
    
    @allure.step('Клик на первый ингредиент')
    def click_first_ingredient(self):
        """Открыть модальное окно с деталями первого ингредиента"""
        self.click_on_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Закрыть модальное окно ингредиента')
    def close_ingredient_modal(self):
        """Закрыть модальное окно с деталями ингредиента"""
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        """Перетащить первый ингредиент в область конструктора бургера"""
        self.drag_and_drop_on_element(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_SECTION
        )

    
    
    @allure.step('Проверка отображения кнопки "Личный кабинет"')
    def is_profile_button_displayed(self) -> bool:
        """Проверить, что кнопка 'Личный кабинет' отображается"""
        return self.check_element_displayed(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Проверка отображения кнопки "Конструктор"')
    def is_constructor_button_displayed(self) -> bool:
        """Проверить, что кнопка 'Конструктор' отображается"""
        return self.check_element_displayed(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка отображения кнопки "Лента заказов"')
    def is_feed_button_displayed(self) -> bool:
        """Проверить, что кнопка 'Лента заказов' отображается"""
        return self.check_element_displayed(MainPageLocators.FEED_BUTTON)

    @allure.step('Проверка отображения заголовка конструктора')
    def is_constructor_title_displayed(self) -> bool:
        """Проверить, что заголовок конструктора отображается"""
        return self.check_element_displayed(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Проверка отображения модального окна с деталями ингредиента')
    def is_ingredient_modal_displayed(self) -> bool:
        """Проверить, что модальное окно с деталями ингредиента отображается"""
        return self.check_element_displayed(MainPageLocators.MODAL_DETAILS)

    @allure.step('Проверка что модальное окно закрыто')
    def is_ingredient_modal_closed(self) -> bool:
        """Проверить, что модальное окно с деталями ингредиента закрыто"""
        return not self.check_element_displayed(MainPageLocators.MODAL_DETAILS)

    @allure.step('Проверка активности кнопки "Оформить заказ"')
    def is_order_button_enabled(self) -> bool:
        """Проверить, что кнопка 'Оформить заказ' активна"""
        return self.is_element_enabled(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверка отображения модального окна с подтверждением заказа')
    def is_order_confirmation_modal_displayed(self) -> bool:
        """Проверить, что модальное окно с подтверждением заказа отображается"""
        return self.check_element_displayed(MainPageLocators.ORDER_SUBMITTED_MODAL)

  
    
    @allure.step('Получение значения счетчика ингредиента')
    def get_ingredient_counter_value(self) -> str:
        """Получить значение счетчика ингредиента"""
        element = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
        return element.text


    
    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        """Нажать кнопку оформления заказа"""
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)