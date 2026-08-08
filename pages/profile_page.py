import allure
from pages.base_page import BasePage
from locators.profile_page_lct import ProfilePageLocators
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    
    @allure.step('Проверка открытия страницы профиля')
    def is_profile_page_opened(self) -> bool:
        
        return self.check_element_displayed(ProfilePageLocators.PROFILE_TAB) or \
               self.check_element_displayed(ProfilePageLocators.PROFILE_NAME_INPUT)
    
    @allure.step('Проверка открытия страницы профиля (старый метод)')
    def check_profile_page_opened(self) -> bool:
        
        return self.is_profile_page_opened()
    
    @allure.step('Проверка открытия страницы истории заказов')
    def is_order_history_page_opened(self) -> bool:
        
        return self.check_element_displayed(ProfilePageLocators.ORDER_HISTORY_TAB)
    
    
    @allure.step('Переход на вкладку "Профиль"')
    def go_to_profile_tab(self):
        
        self.click_on_element(ProfilePageLocators.PROFILE_TAB)
        self.wait_for_page_load()
    
    @allure.step('Переход на вкладку "История заказов"')
    def go_to_order_history_tab(self):
        
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_page_load()
    
    
    @allure.step('Клик на кнопку "Выход"')
    def click_logout_button(self):
        
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Клик на кнопку "Сохранить"')
    def click_save_button(self):
        
        self.click_on_element(ProfilePageLocators.SAVE_BUTTON)
        self.wait_for_page_load()
    
    @allure.step('Клик на кнопку "История заказов"')
    def click_order_history_button(self):
        
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_TAB)
        self.wait_for_page_load()
    
   
    
    @allure.step('Получение имени пользователя')
    def get_user_name(self) -> str:
         
        try:
            element = self.find_element((By.NAME, "name"), timeout=3)
            value = element.get_attribute('value')
            if value and value != "":
                return value
        except Exception:
            pass
        
        try:
            name_labels = self.find_all_elements((By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input"), timeout=3)
            if name_labels:
                value = name_labels[0].get_attribute('value')
                if value and value != "":
                    return value
        except Exception:
            pass
        
        
        try:
            element = self.find_element((By.XPATH, ".//input[@placeholder='Имя']"), timeout=3)
            value = element.get_attribute('value')
            if value and value != "":
                return value
        except Exception:
            pass
        
        
        try:
            
            name_element = self.find_element((By.XPATH, ".//p[contains(text(), 'Имя:')]/following-sibling::p"), timeout=3)
            text = name_element.text
            if text and text != "":
                return text
        except Exception:
            pass
        
        try:
            elements = self.find_all_elements((By.XPATH, ".//p[not(contains(text(), '@'))]"), timeout=3)
            for elem in elements:
                text = elem.text.strip()
                if text and text != "" and len(text) < 50:  # Имя обычно короткое
                    return text
        except Exception:
            pass
        
        return ""
    
    @allure.step('Получение email пользователя')
    def get_user_email(self) -> str:
        
        try:
            element = self.find_element((By.NAME, "email"), timeout=3)
            value = element.get_attribute('value')
            if value:
                return value
        except Exception:
            pass
        
        
        try:
            email_labels = self.find_all_elements((By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input"), timeout=3)
            if email_labels:
                value = email_labels[0].get_attribute('value')
                if value:
                    return value
        except Exception:
            pass
        
       
        try:
            element = self.find_element((By.XPATH, ".//input[@type='email']"), timeout=3)
            value = element.get_attribute('value')
            if value:
                return value
        except Exception:
            pass
        
        
        try:
            inputs = self.find_all_elements((By.XPATH, ".//input"), timeout=3)
            for inp in inputs:
                value = inp.get_attribute('value')
                if value and '@' in value:
                    return value
        except Exception:
            pass
        
        
        try:
            elements = self.find_all_elements((By.XPATH, ".//*[contains(text(), '@')]"), timeout=3)
            for elem in elements:
                text = elem.text
                if text and '@' in text:
                    return text
        except Exception:
            pass
        
        return ""
    
    @allure.step('Получение пароля пользователя')
    def get_user_password(self) -> str:
        """Получить пароль пользователя из профиля."""
        try:
            element = self.find_element(ProfilePageLocators.PROFILE_PASSWORD_INPUT, timeout=3)
            return element.get_attribute('value') or element.text
        except Exception:
            return ""
    
    @allure.step('Получение всех данных из профиля для отладки')
    def get_all_profile_data(self) -> dict:
        
        return {
            'name': self.get_user_name(),
            'email': self.get_user_email(),
            'password': self.get_user_password()
        }