"""
Пакет с локаторами для всех страниц.
"""
from .common_locators import CommonLocators
from .auth_page_lct import AuthPageLocators
from .main_page_lct import MainPageLocators
from .feed_page_lct import FeedPageLocators
from .profile_page_lct import ProfilePageLocators
from .recovery_page_lct import RecoveryPageLocators


class AllLocators:
    """Класс-агрегатор всех локаторов."""
    common = CommonLocators
    auth = AuthPageLocators
    main = MainPageLocators
    feed = FeedPageLocators
    profile = ProfilePageLocators
    recovery = RecoveryPageLocators


__all__ = [
    'CommonLocators',
    'AuthPageLocators',
    'MainPageLocators',
    'FeedPageLocators',
    'ProfilePageLocators',
    'RecoveryPageLocators',
    'AllLocators',
]
