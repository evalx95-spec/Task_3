from selenium.webdriver.common.by import By


class MainPageLocators:

    
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")


    
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")


    
    FIRST_INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")


    
    BURGER_CONSTRUCTOR_SECTION = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    

    BURGER_CONSTRUCTOR_INGREDIENT_ITEM = (
        By.XPATH,
        ".//section[contains(@class, 'BurgerConstructor_basket')]//li[contains(@class, 'BurgerConstructor_basket__listItem')]"
    )
    

    MODAL_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")

    
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_SUBMITTED_MODAL = (By.XPATH, ".//p[contains(text(), 'идентификатор заказа')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")