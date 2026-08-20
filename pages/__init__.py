from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from pages.recovery_password_page import RecoveryPasswordPage
from locators import AllLocators


class UIWorkerWeb(
    MainPage,
    AuthPage,
    OrderFeedPage,
    ProfilePage,
    RecoveryPasswordPage
):
        
    def __init__(self, driver):
        
        super().__init__(driver)
        self.locators = AllLocators


__all__ = [
    'BasePage',
    'AuthPage',
    'MainPage',
    'OrderFeedPage',
    'ProfilePage',
    'RecoveryPasswordPage',
    'UIWorkerWeb',
    'AllLocators',
]
