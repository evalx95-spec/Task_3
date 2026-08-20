import allure
from pages.auth_page import AuthPage                  
from pages.recovery_password_page import RecoveryPasswordPage
from utils.urls import Urls


class TestRecoveryPassword:

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Проверка перехода на страницу /forgot-password через ссылку на странице логина")
    @allure.severity(allure.severity_level.NORMAL)
    def test_go_to_forgot_password_page(self, driver):
        auth_page = AuthPage(driver)
        recovery_page = RecoveryPasswordPage(driver)

        auth_page.open_page(Urls.LOGIN)
        auth_page.click_forgot_password_link()  

        current_url = recovery_page.get_current_url()
        assert Urls.FORGOT_PASS in current_url.lower(), \
            f"Ожидался переход на страницу восстановления, получен URL: {current_url}"

        allure.attach(current_url, name="Текущий URL", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Ввод email для восстановления пароля")
    @allure.description("Проверка ввода email на странице восстановления пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_enter_email_for_reset(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASS)
        recovery_page.enter_email_for_reset_password()

        assert recovery_page.is_email_field_filled(), "Email не был введен"

        allure.attach("Email успешно введен",
                     name="Результат",
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Нажатие кнопки 'Восстановить'")
    @allure.description("Проверка, что при нажатии кнопки 'Восстановить' появляется форма сброса пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_reset_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASS)
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()

        assert recovery_page.is_save_button_displayed(), \
            "Кнопка 'Сохранить' не появилась после восстановления"

        allure.attach("Форма сброса пароля открыта",
                     name="Результат",
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Клик на кнопку 'Показать/скрыть пароль'")
    @allure.description("Проверка, что при клике на кнопку показа пароля поле становится активным")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_show_password_button(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASS)
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()
        recovery_page.click_on_show_password_button()

        assert recovery_page.is_save_button_displayed(), \
            "Страница сброса пароля не открылась"
        assert recovery_page.is_password_field_active(), \
            "Поле пароля не стало активным после нажатия кнопки показа"

        allure.attach("Кнопка показа пароля нажата",
                     name="Результат",
                     attachment_type=allure.attachment_type.TEXT)

    @allure.title("Восстановление пароля с новым паролем")
    @allure.description("Проверка успешного восстановления пароля")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_reset_password_success(self, driver):
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.open_page(Urls.FORGOT_PASS)
        recovery_page.enter_email_for_reset_password()
        recovery_page.click_reset_button()

        assert recovery_page.is_save_button_displayed(), "Кнопка 'Сохранить' не появилась"

        new_password = recovery_page.enter_new_password()
        recovery_page.click_save_button()

        current_url = recovery_page.get_current_url()

        
        assert Urls.FORGOT_PASS not in current_url, \
            f"Ожидалось перенаправление со страницы восстановления, но остались на: {current_url}"

        allure.attach(f"Новый пароль: {new_password}",
                     name="Пароль",
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Текущий URL после сохранения: {current_url}",
                     name="URL после сохранения",
                     attachment_type=allure.attachment_type.TEXT)
        allure.attach("Тест проверяет ввод нового пароля и нажатие кнопки 'Сохранить'",
                     name="Результат",
                     attachment_type=allure.attachment_type.TEXT)
