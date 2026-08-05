import allure
from pages.base_page import BasePage
from locators.auth_page_lct import AuthPageLocators
from locators.main_page_lct import MainPageLocators
from data import TestData


class AuthPage(BasePage):
    
    @allure.step('Кликнуть на кнопку "Войти в аккаунт"')
    def click_login_account_button(self):
        
        self.check_element_displayed(MainPageLocators.PROFILE_BUTTON)
        self.click_on_element(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Заполнить поле "Email" значением: {email}')
    def input_email_field(self, email):
        
        self.check_element_displayed(AuthPageLocators.EMAIL_INPUT)  
        self.click_on_element(AuthPageLocators.EMAIL_INPUT)         
        self.input_text(AuthPageLocators.EMAIL_INPUT, email)        

    @allure.step('Заполнить поле "Пароль"')
    def set_password_field(self, password):
        
        self.check_element_displayed(AuthPageLocators.PASSWORD_INPUT)  
        self.click_on_element(AuthPageLocators.PASSWORD_INPUT)         
        self.input_text(AuthPageLocators.PASSWORD_INPUT, password)     

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        
        self.click_on_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Выполнить авторизацию пользователя {email}')
    def login(self, email, password):
        
        self.click_login_account_button()
        self.input_email_field(email)
        self.set_password_field(password)
        self.click_login_button()
        return self.check_element_displayed(MainPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Авторизация как существующий пользователь')
    def login_as_existing_user(self):
        
        user_data = TestData.EXISTING_USER
        return self.login(user_data['email'], user_data['password'])

    @allure.step('Проверить отображение кнопки "Войти"')
    def is_login_button_displayed(self):
       
        return self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Получить URL текущей страницы')
    def get_login_url(self):
        
        self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)
        return self.get_current_url()

    @allure.step('Проверить что открыта страница авторизации')
    def is_auth_page_opened(self):
        
        return self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка открытия страницы логина')
    def check_login_page_opened(self):
        
        return self.check_element_displayed(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать на ссылку "Восстановить пароль"')
    def click_forgot_password_link(self):
        
        self.check_element_displayed(AuthPageLocators.FORGOT_PASSWORD_LINK)
        self.click_on_element(AuthPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Очистить поле "Email"')
    def clear_email_field(self):
        
        self.clear_field(AuthPageLocators.EMAIL_INPUT)

    @allure.step('Очистить поле "Пароль"')
    def clear_password_field(self):
        
        self.clear_field(AuthPageLocators.PASSWORD_INPUT)

    @allure.step('Ожидание загрузки страницы после авторизации')
    def wait_for_login_complete(self):
        
        return self.check_element_displayed(MainPageLocators.CONFIRM_ORDER_BUTTON)