"""
Page Object для страницы профиля пользователя.
"""
import allure
from pages.base_page import BasePage
from locators.profile_page_lct import ProfilePageLocators


class ProfilePage(BasePage):
    """
    Класс для работы со страницей профиля.
    """

    @allure.step("Клик на вкладку \"История заказов\"")
    def click_orders_history_button(self):
        """Клик на вкладку 'История заказов'."""
        self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_TAB)

    @allure.step("Клик на вкладку \"Профиль\"")
    def click_profile_tab(self):
        """Клик на вкладку 'Профиль'."""
        self.check_element_displayed(ProfilePageLocators.PROFILE_TAB)
        self.click_on_element(ProfilePageLocators.PROFILE_TAB)

    @allure.step("Клик на кнопку \"Выйти\"")
    def click_logout_button(self):
        """Клик на кнопку 'Выйти'."""
        self.check_element_displayed(ProfilePageLocators.LOGOUT_BUTTON)
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Получение URL профиля")
    def get_profile_url(self):
        """Получение URL страницы профиля."""
        self.check_element_displayed(ProfilePageLocators.PROFILE_TAB)
        return self.get_current_url()

    @allure.step("Получение URL истории заказов")
    def get_orders_history_url(self):
        """Получение URL страницы истории заказов."""
        self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_TAB)
        return self.get_current_url()

    @allure.step("Изменение имени на {new_name}")
    def change_name(self, new_name):
        """
        Изменение имени пользователя.
        
        Args:
            new_name (str): Новое имя
        """
        self.check_element_displayed(ProfilePageLocators.PROFILE_NAME_INPUT)
        self.input_text(ProfilePageLocators.PROFILE_NAME_INPUT, new_name)
        self.click_save_button()

    @allure.step("Изменение email на {new_email}")
    def change_email(self, new_email):
        """
        Изменение email пользователя.
        
        Args:
            new_email (str): Новый email
        """
        self.check_element_displayed(ProfilePageLocators.PROFILE_EMAIL_INPUT)
        self.input_text(ProfilePageLocators.PROFILE_EMAIL_INPUT, new_email)
        self.click_save_button()

    @allure.step("Клик на кнопку \"Сохранить\"")
    def click_save_button(self):
        """Клик на кнопку 'Сохранить'."""
        self.check_element_displayed(ProfilePageLocators.SAVE_BUTTON)
        self.click_on_element(ProfilePageLocators.SAVE_BUTTON)

    @allure.step("Проверка, что имя изменилось на {expected_name}")
    def check_name_changed(self, expected_name):
        """
        Проверка, что имя изменилось.
        
        Args:
            expected_name (str): Ожидаемое имя
            
        Returns:
            bool: True если имя совпадает
        """
        element = self.find_element(ProfilePageLocators.PROFILE_NAME_INPUT)
        return element.get_attribute("value") == expected_name

    @allure.step("Проверка, что email изменился на {expected_email}")
    def check_email_changed(self, expected_email):
        """
        Проверка, что email изменился.
        
        Args:
            expected_email (str): Ожидаемый email
            
        Returns:
            bool: True если email совпадает
        """
        element = self.find_element(ProfilePageLocators.PROFILE_EMAIL_INPUT)
        return element.get_attribute("value") == expected_email

    @allure.step("Получение текущего имени")
    def get_current_name(self):
        """
        Получение текущего имени пользователя.
        
        Returns:
            str: Текущее имя
        """
        element = self.find_element(ProfilePageLocators.PROFILE_NAME_INPUT)
        return element.get_attribute("value")

    @allure.step("Получение текущего email")
    def get_current_email(self):
        """
        Получение текущего email пользователя.
        
        Returns:
            str: Текущий email
        """
        element = self.find_element(ProfilePageLocators.PROFILE_EMAIL_INPUT)
        return element.get_attribute("value")

    @allure.step("Проверка открытия страницы профиля")
    def check_profile_page_opened(self):
        """
        Проверка, что страница профиля открыта.
        
        Returns:
            bool: True если страница профиля открыта
        """
        return self.check_element_displayed(ProfilePageLocators.PROFILE_TAB)

    @allure.step("Проверка открытия страницы истории заказов")
    def check_order_history_opened(self):
        """
        Проверка, что страница истории заказов открыта.
        
        Returns:
            bool: True если страница истории заказов открыта
        """
        return self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_TAB)
