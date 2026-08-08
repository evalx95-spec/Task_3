from selenium.webdriver.common.by import By


class FeedPageLocators:
    
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    
    FEED_ORDER_CARD = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li")
    FEED_ORDER_NUMBER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li//p[contains(@class, 'digits-default')]")
    
    COUNTER_DONE_ALL = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    COUNTER_DONE_TODAY = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    IN_PROGRESS_LIST = (By.XPATH, ".//ul[not(contains(@class, 'Ready')) and contains(@class, 'OrderFeed_orderList')]/li")
    IN_PROGRESS_NUMBERS = (By.XPATH, ".//ul[not(contains(@class, 'Ready')) and contains(@class, 'OrderFeed_orderList')]/li/p")
    
    MODAL_ORDER_NUMBER = (By.XPATH, ".//section[contains(@class, 'Modal')]//h2[contains(@class, 'title')]")
    MODAL_ORDER_STATUS = (By.XPATH, ".//section[contains(@class, 'Modal')]//p[contains(text(), 'Выполнен')]")


class OrderHistoryLocators:
   
    HISTORY_ORDER_CARD = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]")
    HISTORY_ORDER_NUMBER = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'digits-default')]")
    HISTORY_ORDER_STATUS = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]//p[contains(text(), 'Готов')]")