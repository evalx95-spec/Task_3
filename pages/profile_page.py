import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.profile_page_lct import ProfilePageLocators


class ProfilePage(BasePage):
    
    @allure.step('Проверка открытия страницы профиля')
    def is_profile_page_opened(self) -> bool:
        """Проверить, что страница профиля открыта."""
        return (self.check_element_displayed(ProfilePageLocators.PROFILE_TAB) or
                self.check_element_displayed(ProfilePageLocators.PROFILE_NAME_INPUT))
    
    @allure.step('Проверка открытия страницы профиля (старый метод)')
    def check_profile_page_opened(self) -> bool:
        """Проверить, что страница профиля открыта (обратная совместимость)."""
        return self.is_profile_page_opened()
    
    @allure.step('Проверка открытия страницы истории заказов')
    def is_order_history_page_opened(self) -> bool:
        """Проверить, что страница истории заказов открыта."""
        return self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_TAB)
    
    @allure.step('Переход на вкладку "Профиль"')
    def go_to_profile_tab(self):
        """Перейти на вкладку "Профиль"."""
        self.click_on_element(ProfilePageLocators.PROFILE_TAB)
        self.wait_for_page_load()
    
    @allure.step('Переход на вкладку "История заказов"')
    def go_to_order_history_tab(self):
        """Перейти на вкладку "История заказов"."""
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_page_load()
    
    @allure.step('Клик на кнопку "Выход"')
    def click_logout_button(self):
        """Нажать на кнопку "Выход"."""
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Клик на кнопку "Сохранить"')
    def click_save_button(self):
        """Нажать на кнопку "Сохранить"."""
        self.click_on_element(ProfilePageLocators.SAVE_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Клик на кнопку "История заказов"')
    def click_order_history_button(self):
        """Нажать на кнопку "История заказов"."""
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_page_load()
    
    @allure.step('Получение имени пользователя')
    def get_user_name(self, timeout=10) -> str:
        """Получить имя пользователя из профиля."""
        try:
            
            element = self.find_element(ProfilePageLocators.PROFILE_NAME_INPUT, timeout=timeout)
            value = element.get_attribute('value')
            return value.strip() if value else ""
        except Exception:
            return ""
    
    @allure.step('Получение email пользователя')
    def get_user_email(self, timeout=10) -> str:
       
        element = self.find_element(ProfilePageLocators.PROFILE_EMAIL_INPUT, timeout=timeout)
        
       
        wait = WebDriverWait(self.driver, timeout)
        email = wait.until(lambda d: element.get_attribute("value").strip())
        
        return email
    
    @allure.step('Получение пароля пользователя')
    def get_user_password(self, timeout=10) -> str:
        """Получить пароль пользователя из профиля."""
        try:
            element = self.find_element(ProfilePageLocators.PROFILE_PASSWORD_INPUT, timeout=timeout)
            value = element.get_attribute('value')
            if value:
                return value.strip()
            return element.text.strip() if element.text else ""
        except Exception:
            return ""