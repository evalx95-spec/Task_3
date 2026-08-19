BASE_URL = "https://qa-stellarburgers.education-services.ru"
BASE_API_URL = "https://qa-stellarburgers.education-services.ru"


class Urls:
    
    HOME = BASE_URL
    LOGIN = BASE_URL + '/login'
    REGISTER = BASE_URL + '/register'
    FORGOT_PASS = BASE_URL + '/forgot-password'
    RESET_PASS = BASE_URL + '/reset-password'
    FEED = BASE_URL + '/feed'
    
    PROFILE = BASE_URL + '/account/profile'
    ORDERS_HISTORY = BASE_URL + '/account/order-history'
    
    @classmethod
    def get_full_url(cls, path: str) -> str:
        """Получить полный URL для указанного пути."""
        if path.startswith('http'):
            return path
        return BASE_URL + path


class ApiEndpoints:
    """API эндпоинты."""
    
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    UPDATE_USER = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    LOGOUT_USER = '/api/auth/logout'
    
    CREATE_ORDER = '/api/orders'
    GET_USER_ORDERS = '/api/orders'
    GET_ALL_ORDERS = '/api/orders/all'
    
    GET_INGREDIENTS = '/api/ingredients'
    
    @classmethod
    def get_full_url(cls, endpoint: str) -> str:
        """Получить полный URL для указанного эндпоинта."""
        if endpoint.startswith('http'):
            return endpoint
        return BASE_API_URL + endpoint


class Pages:
    """Полные URL-адреса для проверок."""
    
    HOME = BASE_URL + '/'
    LOGIN = BASE_URL + '/login'
    REGISTER = BASE_URL + '/register'
    FORGOT_PASS = BASE_URL + '/forgot-password'
    RESET_PASS = BASE_URL + '/reset-password'
    PROFILE = BASE_URL + '/account/profile'
    ORDERS_HISTORY = BASE_URL + '/account/order-history'
    FEED = BASE_URL + '/feed'
    
    @classmethod
    def get_all_pages(cls) -> list:
        """Получить список всех URL-адресов страниц."""
        return [
            cls.HOME,
            cls.LOGIN,
            cls.REGISTER,
            cls.FORGOT_PASS,
            cls.RESET_PASS,
            cls.PROFILE,
            cls.ORDERS_HISTORY,
            cls.FEED
        ]