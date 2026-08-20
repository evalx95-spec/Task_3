import allure
from pages.base_page import BasePage
from locators.order_feed_page_lct import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть на заказ в списке заказов')
    def click_order(self):
        self.assert_element_visible(OrderFeedPageLocators.ORDER, "Заказ не отображается")
        self.click_element(OrderFeedPageLocators.ORDER)

    @allure.step('Получение состава заказа')
    def get_text_order_structure(self):
        self.wait_for_element_visible(OrderFeedPageLocators.ORDER_STRUCTURE)
        return self.get_text(OrderFeedPageLocators.ORDER_STRUCTURE)

    @allure.step('Поиск заказа по номеру')
    def check_order_id(self, order_id, locator):
        elements = self.find_elements(locator)
        for element in elements:
            if order_id == element.text:
                return True
        return False

    @allure.step('Проверить наличие созданного заказа в разделе "История заказов"')
    def order_id_found_in_history_orders(self, order_number):
        return self.check_order_id(order_number, OrderFeedPageLocators.HISTORY_ORDERS)

    @allure.step('Проверить наличие созданного заказа в "Ленте заказов"')
    def order_id_found_in_order_feed(self, order_number):
        return self.check_order_id(order_number, OrderFeedPageLocators.FEED_ORDERS)

    @allure.step('Получить номер последнего заказа из раздела "В работе"')
    def get_user_order_in_progress(self):
        self.wait_for_condition(
            lambda driver: self.get_text(OrderFeedPageLocators.NUMBER_IN_PROGRESS) != 'Все текущие заказы готов!',
            message="Заказ в работе не появился"
        )
        order = self.get_text(OrderFeedPageLocators.NUMBER_IN_PROGRESS)
        return order.lstrip('0')

    @allure.step('Получить количество заказов')
    def get_total_order_count(self, locator):
        return self.get_text(locator)

    