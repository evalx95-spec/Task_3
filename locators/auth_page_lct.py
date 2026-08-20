from selenium.webdriver.common.by import By

class AuthPageLocators:
    
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    

    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")
    
   
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")