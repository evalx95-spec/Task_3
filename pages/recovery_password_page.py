import allure
from faker import Faker
from pages.base_page import BasePage
from locators.recovery_page_lct import RecoveryPageLocators
from locators.auth_page_lct import AuthPageLocators
from utils.urls import Urls
from data import TestData


class RecoveryPasswordPage(BasePage):
    
    @allure.step('Переход на страницу восстановления пароля')
    def go_to_forgot_password_page(self):
        
        self.open_page(Urls.FORGOT_PASS)

    @allure.step('Клик по ссылке "Восстановить пароль"')
    def click_password_reset_link(self):
        
        self.open_page(Urls.LOGIN)
        self.click_on_element(AuthPageLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step('Ввод email для восстановления пароля: {email}')
    def enter_email_for_reset_password(self, email=None):
        
        if email is None:
            email = TestData.EXISTING_USER['email']
        self.input_text(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод нового пароля')
    def enter_new_password(self, password=None):
        
        if password is None:
            fake = Faker()
            password = fake.password(length=10)
        self.input_text(RecoveryPageLocators.PASSWORD_INPUT, password)
        return password

    @allure.step('Ввод кода из письма')
    def enter_reset_code(self, code):
        
        self.input_text(RecoveryPageLocators.CODE_INPUT, code)

    
    @allure.step('Нажатие кнопки "Восстановить"')
    def click_reset_button(self):
        
        self.check_element_displayed(RecoveryPageLocators.RESTORE_BUTTON)
        self.click_on_element(RecoveryPageLocators.RESTORE_BUTTON)

    @allure.step('Клик на кнопку "Показать/скрыть пароль"')
    def click_on_show_password_button(self):
        
        self.check_element_displayed(RecoveryPageLocators.EYE_BUTTON)
        self.click_on_element(RecoveryPageLocators.EYE_BUTTON)

    @allure.step('Нажатие кнопки "Сохранить"')
    def click_save_button(self):
        
        self.click_on_element(RecoveryPageLocators.SAVE_BUTTON)

    
    @allure.step('Проверка отображения кнопки "Сохранить"')
    def is_save_button_displayed(self) -> bool:
        
        return self.check_element_displayed(RecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def find_save_button(self):
    
        return self.is_save_button_displayed()

    @allure.step('Проверка что поле Email заполнено')
    def is_email_field_filled(self) -> bool:
        
        element = self.find_element(RecoveryPageLocators.EMAIL_INPUT)
        return element.get_attribute('value') != ""

    @allure.step('Проверка что поле пароля активно')
    def is_password_field_active(self) -> bool:
        
        element = self.find_element(RecoveryPageLocators.PASSWORD_INPUT)
        return element == self.driver.switch_to.active_element

    @allure.step('Поиск активного поля "Пароль"')
    def find_input_active(self):
        
        return self.check_element_displayed(RecoveryPageLocators.PASSWORD_FIELD_CONTAINER)

    @allure.step('Проверка успешного восстановления пароля')
    def is_auth_page_opened(self) -> bool:
        
        return self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка успешного восстановления пароля')
    def check_password_reset_success(self):
        
        return self.is_auth_page_opened()

    
    @allure.step('Полный процесс восстановления пароля')
    def reset_password(self, email=None, new_password=None, code=None):
        
        self.enter_email_for_reset_password(email)
        self.click_reset_button()
        
        if code:
            self.enter_reset_code(code)
        
        if new_password is None:
            new_password = self.enter_new_password()
        else:
            self.enter_new_password(new_password)
        
        self.click_save_button()
        return new_password