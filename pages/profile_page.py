import allure
from pages.base_page import BasePage
from locators.profile_page_lct import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step('Проверка открытия страницы профиля')
    def is_profile_page_opened(self) -> bool:
        """Проверить, что страница профиля открыта."""
        return (
            self.is_element_visible(ProfilePageLocators.PROFILE_TAB) or
            self.is_element_visible(ProfilePageLocators.PROFILE_NAME_INPUT)
        )

    @allure.step('Проверка открытия страницы истории заказов')
    def is_order_history_page_opened(self) -> bool:
        """Проверить, что страница истории заказов открыта."""
        return self.is_element_visible(ProfilePageLocators.ORDER_HISTORY_TAB)

    @allure.step('Переход на вкладку "Профиль"')
    def go_to_profile_tab(self):
        """Перейти на вкладку "Профиль"."""
        self.assert_element_visible(ProfilePageLocators.PROFILE_TAB, "Вкладка «Профиль» не отображается")
        self.click_element(ProfilePageLocators.PROFILE_TAB)

    @allure.step('Клик на кнопку "История заказов"')
    def click_order_history_button(self):
        """Нажать на кнопку "История заказов"."""
        self.assert_element_visible(ProfilePageLocators.ORDER_HISTORY_TAB, "Вкладка «История заказов» не отображается")
        self.click_element(ProfilePageLocators.ORDER_HISTORY_TAB)

    @allure.step('Клик на кнопку "Выход"')
    def click_logout_button(self):
        """Нажать на кнопку "Выход"."""
        self.assert_element_visible(ProfilePageLocators.LOGOUT_BUTTON, "Кнопка «Выход» не отображается")
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Клик на кнопку "Сохранить"')
    def click_save_button(self):
        """Нажать на кнопку "Сохранить"."""
        self.assert_element_visible(ProfilePageLocators.SAVE_BUTTON, "Кнопка «Сохранить» не отображается")
        self.click_element(ProfilePageLocators.SAVE_BUTTON)

    @allure.step('Получение имени пользователя')
    def get_user_name(self, timeout=10) -> str:
        """Получить имя пользователя из профиля."""
        return self.get_input_value(ProfilePageLocators.PROFILE_NAME_INPUT, timeout)

    @allure.step('Получение email пользователя')
    def get_user_email(self, timeout=10) -> str:
        """Получить email пользователя из профиля."""
        return self.get_input_value(ProfilePageLocators.PROFILE_EMAIL_INPUT, timeout)

    @allure.step('Получение пароля пользователя')
    def get_user_password(self, timeout=10) -> str:
        """Получить пароль пользователя из профиля."""
        return self.get_input_value(ProfilePageLocators.PROFILE_PASSWORD_INPUT, timeout)
