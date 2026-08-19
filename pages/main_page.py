import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_lct import MainPageLocators


class MainPage(BasePage):

   
    @allure.step('Проверка отображения кнопки "Личный кабинет"')
    def is_profile_button_displayed(self) -> bool:
        return self.is_element_visible(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Проверка отображения кнопки "Конструктор"')
    def is_constructor_button_displayed(self) -> bool:
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверка отображения кнопки "Лента заказов"')
    def is_feed_button_displayed(self) -> bool:
        return self.is_element_visible(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик на кнопку "Личный кабинет"')
    def click_profile_button(self):
        self.click_element(MainPageLocators.PROFILE_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на кнопку "Лента заказов"')
    def click_feed_button(self):
        self.click_element(MainPageLocators.FEED_BUTTON)
        self.wait_for_page_load()

    @allure.step('Клик на первый ингредиент')
    def click_first_ingredient(self):
        element = self.wait_for_element_clickable(
            MainPageLocators.FIRST_INGREDIENT,
            timeout=self.long_timeout
        )
        self.scroll_to_element(element)
        self.click_via_js(element)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        close_button = self.wait_for_element_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.scroll_to_element(close_button)
        close_button.click()
        self.wait_for_element_invisible(MainPageLocators.MODAL_DETAILS)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop_on_element(
            MainPageLocators.FIRST_INGREDIENT,
            MainPageLocators.BURGER_CONSTRUCTOR_SECTION
        )

    @allure.step('Очистить корзину конструктора')
    def clear_constructor_basket(self):
        """Очищает корзину конструктора через localStorage и refresh"""
        self.clear_local_storage()
        self.refresh_page()
        self.wait_for_element_visible(
            MainPageLocators.FIRST_INGREDIENT,
            timeout=self.long_timeout
        )

    @allure.step('Проверить, что ингредиент отображается в корзине конструктора')
    def is_ingredient_in_basket(self) -> bool:
        """Проверить, что в корзине есть хотя бы один ингредиент"""
        elements = self.find_elements(MainPageLocators.BURGER_CONSTRUCTOR_INGREDIENT_ITEM)
        return len(elements) > 0

    @allure.step('Проверка отображения заголовка конструктора')
    def is_constructor_title_displayed(self) -> bool:
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Проверка отображения модального окна с деталями ингредиента')
    def is_ingredient_modal_displayed(self) -> bool:
        return self.is_element_visible(MainPageLocators.MODAL_DETAILS)

    @allure.step('Проверка, что модальное окно закрыто')
    def is_ingredient_modal_closed(self) -> bool:
        return not self.is_element_visible(MainPageLocators.MODAL_DETAILS)

    @allure.step('Ждать появления ингредиентов в корзине')
    def wait_for_ingredient_in_basket(self, min_count=1, timeout=10):
        """Ждать, пока в корзине появится хотя бы min_count ингредиентов"""
        self.wait_for_at_least_n_elements(
            MainPageLocators.BURGER_CONSTRUCTOR_INGREDIENT_ITEM,
            min_count=min_count,
            timeout=timeout
        )