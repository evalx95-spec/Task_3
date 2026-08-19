import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains
from utils.urls import BASE_URL


class BasePage:
    
    def __init__(self, driver, base_url=None):
        self.driver = driver
        
        if base_url is None:
            self.base_url = BASE_URL
        else:
            self.base_url = base_url
        self.default_timeout = 10
        self.long_timeout = 20
    
    
    def create_wait(self, timeout=None):
        """Создать WebDriverWait с указанным или стандартным таймаутом"""
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout)
    
    def wait_for_element_visible(self, locator, timeout=None):
        """Ждать, пока элемент станет видимым"""
        wait = self.create_wait(timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_present(self, locator, timeout=None):
        """Ждать, пока элемент появится в DOM"""
        wait = self.create_wait(timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """Ждать, пока элемент станет кликабельным"""
        wait = self.create_wait(timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_element_invisible(self, locator, timeout=None):
        """Ждать, пока элемент исчезнет"""
        wait = self.create_wait(timeout)
        return wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_element_not_present(self, locator, timeout=None):
        """Ждать, пока элемент исчезнет из DOM"""
        wait = self.create_wait(timeout)
        return wait.until_not(EC.presence_of_element_located(locator))
    
    def wait_for_condition(self, condition, timeout=None, message=""):
        """Ждать выполнения произвольного условия"""
        wait = self.create_wait(timeout)
        return wait.until(condition, message)
    
    def wait_for_page_load(self):
        """Ждать полной загрузки страницы"""
        wait = self.create_wait()
        return wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
    
    def wait_for_at_least_n_elements(self, locator, min_count=1, timeout=None):
        """Ждать, пока количество элементов по локатору не станет >= min_count"""
        wait = self.create_wait(timeout)
        
        def condition(driver):
            elements = self.find_elements(locator)
            return len(elements) >= min_count
        
        wait.until(condition, f"Количество элементов меньше {min_count}")
        return self.find_elements(locator)
    
    
    def click_element(self, locator, timeout=None):
        """Кликнуть по элементу с ожиданием кликабельности"""
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()
        return element
    
    def click_via_js(self, element):
        """Кликнуть через JavaScript"""
        self.driver.execute_script("arguments[0].click();", element)
    
    def input_text(self, locator, text, timeout=None):
        """Ввести текст в поле с ожиданием видимости"""
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)
        return element
    
    def clear_field(self, locator, timeout=None):
        """Очистить поле ввода"""
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        return element
    
    def get_text(self, locator, timeout=None):
        """Получить текст элемента"""
        element = self.wait_for_element_visible(locator, timeout)
        return element.text
    
    def get_attribute(self, locator, attribute, timeout=None):
        """Получить значение атрибута элемента"""
        element = self.wait_for_element_present(locator, timeout)
        return element.get_attribute(attribute)
    
    def get_input_value(self, locator, timeout=None):
        """Получить значение из поля ввода"""
        try:
            return self.get_attribute(locator, 'value', timeout) or ""
        except:
            return ""
    
    
    def is_element_visible(self, locator, timeout=None) -> bool:
        """Проверить, отображается ли элемент"""
        try:
            self.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=None) -> bool:
        """Проверить, присутствует ли элемент в DOM"""
        try:
            self.wait_for_element_present(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_not_visible(self, locator, timeout=None) -> bool:
        """Проверить, что элемент не отображается"""
        try:
            self.wait_for_element_invisible(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    def is_element_not_present(self, locator, timeout=None) -> bool:
        """Проверить, что элемент отсутствует в DOM"""
        try:
            self.wait_for_element_not_present(locator, timeout)
            return True
        except TimeoutException:
            return False
    
    
    def open_page(self, url=None):
        """Открыть указанную страницу или базовый URL"""
        target_url = url if url else self.base_url
        
        
        if not target_url:
            raise ValueError(f"URL не может быть пустым. Переданный URL: {target_url}")
        
        
        if not isinstance(target_url, str):
            raise TypeError(f"URL должен быть строкой. Получен тип: {type(target_url)}")
        
        
        if target_url.startswith('/'):
            target_url = BASE_URL + target_url
        
       
        print(f"Открываю страницу: {target_url}")
        
        try:
            self.driver.get(target_url)
            self.wait_for_page_load()
        except InvalidArgumentException as e:
            raise InvalidArgumentException(f"Не удалось открыть URL: {target_url}. Ошибка: {e}")
    
    def refresh_page(self):
        """Обновить страницу"""
        self.driver.refresh()
        self.wait_for_page_load()
    
    def get_current_url(self) -> str:
        """Получить текущий URL страницы"""
        return self.driver.current_url
    
   
    def scroll_to_element(self, element):
        """Прокрутить страницу к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_to_locator(self, locator, timeout=None):
        """Прокрутить страницу к элементу по локатору"""
        element = self.wait_for_element_present(locator, timeout)
        self.scroll_to_element(element)
        return element
    
    
    def find_element(self, locator, timeout=None):
        """Найти элемент"""
        return self.wait_for_element_present(locator, timeout)
    
    def find_elements(self, locator):
        """Найти все элементы по локатору"""
        return self.driver.find_elements(*locator)
    
    def get_element_count(self, locator):
        """Получить количество элементов по локатору"""
        return len(self.find_elements(locator))
    
    def drag_and_drop_on_element(self, source_locator, target_locator):
        """Перетащить элемент"""
        source = self.wait_for_element_visible(source_locator)
        target = self.wait_for_element_visible(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
    
    
    def clear_local_storage(self):
        """Очистить localStorage браузера"""
        self.driver.execute_script("window.localStorage.clear();")
    
    
    def get_active_element(self):
        """Получить активный элемент на странице"""
        return self.driver.switch_to.active_element
    
    def is_element_active(self, locator, timeout=None) -> bool:
        """Проверить, является ли элемент активным"""
        element = self.wait_for_element_present(locator, timeout)
        active_element = self.get_active_element()
        return element == active_element
    
    
    def assert_element_visible(self, locator, message="Элемент не отображается"):
        """Проверить, что элемент отображается, иначе выбросить AssertionError"""
        assert self.is_element_visible(locator), message
    
    def assert_element_not_visible(self, locator, message="Элемент отображается"):
        """Проверить, что элемент не отображается, иначе выбросить AssertionError"""
        assert self.is_element_not_visible(locator), message