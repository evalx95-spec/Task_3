from selenium.webdriver.common.by import By


class FeedPageLocators:
    """Локаторы страницы ленты заказов."""
    
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
