from selenium.webdriver.common.by import By


class RecoveryPageLocators:
   
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    CODE_INPUT = (By.XPATH, ".//label[text()='Введите код из письма']/following-sibling::input")
    
    
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    
   
    EYE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input_type_password')]//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_CONTAINER = (By.XPATH, ".//div[contains(@class, 'input_type_password')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, ".//div[contains(@class, 'input_type_password') and contains(@class, 'input_status_active')]")
    
    RECOVERY_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")