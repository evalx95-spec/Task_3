from selenium.webdriver.common.by import By


class ProfilePageLocators:
    """Локаторы страницы профиля."""
    
    PROFILE_TAB = (By.XPATH, ".//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
