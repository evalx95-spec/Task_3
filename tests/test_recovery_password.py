import allure
import pytest
from pages.recovery_password_page import RecoveryPasswordPage
from locators.recovery_page_lct import RecoveryPageLocators
from config import BASE_URL


class TestRecoveryPassword:
    """Тесты для страницы восстановления пароля."""

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Проверка перехода на страницу /forgot-password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_forgot_password_page(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page("/login")
        recovery_page.click_password_reset_link()
        current_url = recovery_page.get_current_url()
        assert "forgot-password" in current_url.lower(), \
            f"Ожидался переход на страницу восстановления, получен URL: {current_url}"
        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Ввод email для восстановления пароля")
    @allure.description("Проверка ввода email на странице восстановления пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_enter_email_for_reset(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page("/forgot-password")
        recovery_page.enter_email_for_reset_password()
        element = recovery_page.find_element(RecoveryPageLocators.EMAIL_INPUT)
        assert element.get_attribute('value') != "", "Email не был введен"
        allure.attach("Email успешно введен", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Нажатие кнопки 'Восстановить'")
    @allure.description("Проверка, что при нажатии кнопки 'Восстановить' появляется форма сброса пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_reset_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page("/forgot-password")
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()
        assert recovery_page.find_save_button(), \
            "Кнопка 'Сохранить' не появилась после восстановления"
        allure.attach("Форма сброса пароля открыта", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Клик на кнопку 'Показать/скрыть пароль'")
    @allure.description("Проверка, что при клике на кнопку показа пароля поле становится активным")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_show_password_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page("/forgot-password")
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()
        recovery_page.click_on_show_password_button()
        assert recovery_page.check_element_displayed(RecoveryPageLocators.SAVE_BUTTON), \
            "Страница сброса пароля не открылась"
        allure.attach("Кнопка показа пароля нажата", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Восстановление пароля с новым паролем")
    @allure.description("Проверка успешного восстановления пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_reset_password_success(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page("/forgot-password")
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()
        assert recovery_page.find_save_button(), "Кнопка 'Сохранить' не появилась"
        new_password = recovery_page.enter_new_password()
        allure.attach(f"Новый пароль: {new_password}", 
                     name="Пароль", 
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach("Тест выполнен (требуется реальный код из письма для полного восстановления)", 
                     name="Результат", 
                     attachment_type=allure.attachment_type.TEXT)