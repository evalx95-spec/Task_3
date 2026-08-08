import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config import DEFAULT_TIMEOUT
from utils.urls import BASE_URL  
from locators.base_page_lct import BasePageLocators


class BasePage:
    """Базовый класс для всех Page Object классов."""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT or 10)
        self.locators = BasePageLocators()

    
    @allure.step('Переход на страницу: {url}')
    def open_page(self, url: str = None):
       
        full_url = BASE_URL + url if url else BASE_URL
        self.driver.get(full_url)
        self.wait_for_page_load()

    @allure.step('Ожидание загрузки страницы')
    def wait_for_page_load(self):
        """Ожидать полной загрузки страницы."""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step('Обновление страницы')
    def refresh_page(self):
        """Обновить текущую страницу."""
        self.driver.refresh()
        self.wait_for_page_load()

    @allure.step('Получение текущего URL страницы')
    def get_current_url(self) -> str:
        """Получить URL текущей страницы."""
        return self.driver.current_url

    @allure.step('Получение заголовка страницы')
    def get_page_title(self) -> str:
        """Получить заголовок текущей страницы."""
        return self.driver.title

    
    @allure.step('Клик по элементу: {locator}')
    def click_on_element(self, locator):
       
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            try:
                
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as e:
                allure.attach(str(e), name="Ошибка клика", attachment_type=allure.attachment_type.TEXT)
                raise

    @allure.step('Ввод текста "{text}" в поле: {locator}')
    def input_text(self, locator, text: str):
        
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step('Очистка поля: {locator}')
    def clear_field(self, locator):
     
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()

    @allure.step('Получение текста элемента: {locator}')
    def get_element_text(self, locator) -> str:
       
        element = self.find_element(locator)
        return element.text

    @allure.step('Получение значения атрибута элемента: {locator}')
    def get_element_attribute(self, locator, attribute: str) -> str:
       
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    
    
    @allure.step('Нахождение элемента: {locator}')
    def find_element(self, locator, timeout: int = None):
      
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT or 10)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step('Нахождение всех элементов: {locator}')
    def find_all_elements(self, locator, timeout: int = None):
       
        wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT or 10)
        return wait.until(EC.presence_of_all_elements_located(locator))

    
    
    @allure.step('Проверка отображения элемента: {locator}')
    def check_element_displayed(self, locator, timeout: int = None) -> bool:
        
        try:
            wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT or 10)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    @allure.step('Проверка отсутствия элемента: {locator}')
    def check_element_not_displayed(self, locator, timeout: int = None) -> bool:
        
        try:
            wait = WebDriverWait(self.driver, timeout or DEFAULT_TIMEOUT or 10)
            return wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False

    @allure.step('Проверка что элемент активен: {locator}')
    def is_element_enabled(self, locator) -> bool:
       
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except NoSuchElementException:
            return False

    @allure.step('Проверка что элемент выбран: {locator}')
    def is_element_selected(self, locator) -> bool:
        
        element = self.find_element(locator)
        return element.is_selected()

    
    @allure.step('Прокрутка к элементу')
    def scroll_to_element(self, element):
        
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});", 
            element
        )

    @allure.step('Прокрутка к элементу по локатору')
    def scroll_to_element_by_locator(self, locator):
        
        element = self.find_element(locator)
        self.scroll_to_element(element)

    
    
    @allure.step('Drag-and-drop элемента {source_locator} на {target_locator}')
    def drag_and_drop_on_element(self, source_locator, target_locator):
        
        source = self.wait.until(EC.element_to_be_clickable(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        self.scroll_to_element(target)
        self.scroll_to_element(source)
        
        script = """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            
            function fire(element, type, coords) {
                element.dispatchEvent(new DragEvent(type, Object.assign({
                    bubbles: true,
                    cancelable: true,
                    composed: true,
                    dataTransfer: dataTransfer
                }, coords)));
            }
            
            function centerOf(element) {
                const rect = element.getBoundingClientRect();
                return {
                    clientX: rect.left + rect.width / 2,
                    clientY: rect.top + rect.height / 2
                };
            }
            
            const from = centerOf(source);
            const to = centerOf(target);
            
            fire(source, 'dragstart', from);
            fire(target, 'dragenter', to);
            fire(target, 'dragover', to);
            fire(target, 'drop', to);
            fire(source, 'dragend', to);
        """
        self.driver.execute_script(script, source, target)
        
        import time
        time.sleep(0.5)

  
    
    @allure.step('Скриншот страницы')
    def take_screenshot(self, name: str = "screenshot"):
        
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)