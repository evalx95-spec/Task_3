from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_TITLE = (By.XPATH, ".//h2[text()='Профиль']")
    ORDER_HISTORY_TITLE = (By.XPATH, ".//h2[text()='История заказов']")

    PROFILE_TAB = (By.XPATH, ".//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, ".//a[text()='История заказов']")

    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

    
    PROFILE_NAME_INPUT = (By.NAME, "name")

    PROFILE_EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[name='name'][type='text'][disabled]"
    )

    PROFILE_PASSWORD_INPUT = (By.NAME, "password")

    PROFILE_CONTAINER = (By.CLASS_NAME, "profile__container")
    PROFILE_MAIN = (By.CLASS_NAME, "profile__main")

    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'error')]")
    SUCCESS_MESSAGE = (By.XPATH, ".//p[contains(@class, 'success')]")

    USER_AVATAR = (By.XPATH, ".//div[contains(@class, 'avatar')]")
    USER_ID = (By.XPATH, ".//p[contains(@class, 'user-id')]")