from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    
    
    ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    FEED_ORDERS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li//p[contains(@class, 'digits-default')]")
    
    
    HISTORY_ORDERS = (By.XPATH, ".//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'digits-default')]")
    
   
    ORDER_STRUCTURE = (By.XPATH, ".//section[contains(@class, 'Modal')]//div[contains(@class, 'text_type_main-medium')]")
    
    
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[not(contains(@class, 'Ready')) and contains(@class, 'OrderFeed_orderList')]/li[1]")
    COUNTER_DONE_ALL = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    COUNTER_DONE_TODAY = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")