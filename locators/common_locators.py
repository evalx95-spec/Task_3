from selenium.webdriver.common.by import By


class CommonLocators:
    
    
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
    MODAL_VISIBLE = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    HEADER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    HEADER_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
