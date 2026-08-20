import allure
from pages.base_page import BasePage
from locators.auth_page_lct import AuthPageLocators
from data import TestData


class AuthPage(BasePage):

    @allure.step('Заполнить поле "Email" значением: {email}')
    def input_email_field(self, email):
        self.input_text(AuthPageLocators.EMAIL_INPUT, email)

    @allure.step('Заполнить поле "Пароль"')
    def set_password_field(self, password):
        self.input_text(AuthPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажать кнопку "Войти"')
    def click_login_button(self):
        self.assert_element_visible(AuthPageLocators.LOGIN_BUTTON, "Кнопка Войти не отображается")
        self.click_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Выполнить авторизацию пользователя {email}')
    def login(self, email, password):
        self.input_email_field(email)
        self.set_password_field(password)
        self.click_login_button()

    @allure.step('Авторизация как существующий пользователь')
    def login_as_existing_user(self):
        user_data = TestData.EXISTING_USER
        self.login(user_data['email'], user_data['password'])

    @allure.step('Проверить что открыта страница авторизации')
    def is_auth_page_opened(self) -> bool:
        return self.is_element_visible(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать на ссылку "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.assert_element_visible(AuthPageLocators.FORGOT_PASSWORD_LINK, "Ссылка 'Восстановить пароль' не отображается")
        self.click_element(AuthPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Очистить поле "Email"')
    def clear_email_field(self):
        self.clear_field(AuthPageLocators.EMAIL_INPUT)

    @allure.step('Очистить поле "Пароль"')
    def clear_password_field(self):
        self.clear_field(AuthPageLocators.PASSWORD_INPUT)
