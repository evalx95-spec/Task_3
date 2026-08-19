import allure
from faker import Faker
from pages.base_page import BasePage
from locators.recovery_page_lct import RecoveryPageLocators
from utils.urls import Urls
from data import TestData


class RecoveryPasswordPage(BasePage):
    """Класс для работы со страницей восстановления пароля."""

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_forgot_password_page(self):
        """Перейти на страницу восстановления пароля."""
        self.open_page(Urls.FORGOT_PASS)

    @allure.step('Ввод email для восстановления пароля: {email}')
    def enter_email_for_reset_password(self, email=None):
        """Ввести email для восстановления пароля."""
        if email is None:
            email = TestData.EXISTING_USER['email']
        self.assert_element_visible(RecoveryPageLocators.EMAIL_INPUT, "Поле Email не отображается")
        self.input_text(RecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод нового пароля')
    def enter_new_password(self, password=None):
        """Ввести новый пароль."""
        if password is None:
            fake = Faker()
            password = fake.password(length=10)
        self.assert_element_visible(RecoveryPageLocators.PASSWORD_INPUT, "Поле пароля не отображается")
        self.input_text(RecoveryPageLocators.PASSWORD_INPUT, password)
        return password

    @allure.step('Ввод кода из письма')
    def enter_reset_code(self, code):
        """Ввести код из письма."""
        self.assert_element_visible(RecoveryPageLocators.CODE_INPUT, "Поле ввода кода не отображается")
        self.input_text(RecoveryPageLocators.CODE_INPUT, code)

    @allure.step('Нажатие кнопки "Восстановить"')
    def click_reset_button(self):
        """Нажать на кнопку "Восстановить"."""
        self.assert_element_visible(RecoveryPageLocators.RESTORE_BUTTON, "Кнопка 'Восстановить' не отображается")
        self.click_element(RecoveryPageLocators.RESTORE_BUTTON)  

    @allure.step('Клик на кнопку "Показать/скрыть пароль"')
    def click_on_show_password_button(self):
        """Нажать на кнопку показать/скрыть пароль."""
        self.assert_element_visible(RecoveryPageLocators.EYE_BUTTON, "Кнопка показа пароля не отображается")
        self.click_element(RecoveryPageLocators.EYE_BUTTON)  

    @allure.step('Нажатие кнопки "Сохранить"')
    def click_save_button(self):
        """Нажать на кнопку "Сохранить"."""
        self.assert_element_visible(RecoveryPageLocators.SAVE_BUTTON, "Кнопка 'Сохранить' не отображается")
        self.click_element(RecoveryPageLocators.SAVE_BUTTON)  

    @allure.step('Проверка отображения кнопки "Сохранить"')
    def is_save_button_displayed(self) -> bool:
        """Проверить, что кнопка "Сохранить" отображается."""
        return self.is_element_visible(RecoveryPageLocators.SAVE_BUTTON)

    @allure.step('Проверка что поле Email заполнено')
    def is_email_field_filled(self) -> bool:
        """Проверить, что поле Email заполнено."""
        return self.get_input_value(RecoveryPageLocators.EMAIL_INPUT) != ""

    @allure.step('Проверка что поле пароля активно')
    def is_password_field_active(self) -> bool:
        """Проверить, что поле пароля активно."""
        return self.is_element_active(RecoveryPageLocators.PASSWORD_INPUT)

    @allure.step('Полный процесс восстановления пароля')
    def reset_password(self, email=None, new_password=None, code=None):
        """
        Выполнить полный процесс восстановления пароля.
        """
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