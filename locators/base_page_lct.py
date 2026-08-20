from selenium.webdriver.common.by import By

class BasePageLocators:
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")