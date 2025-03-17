import pytest
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from config.config import TestConfig
from utils.logger import Logger

# Настройка логгера
logger = Logger.setup_logger(name="login_tests")

class TestLogin:
    """
    Тесты для страницы авторизации.
    """
    
    def test_successful_login(self, page):
        """
        Тест успешной авторизации.
        """
        logger.info("Начало теста успешной авторизации")
        
        # Создание объектов страниц
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        
        # Шаги теста
        login_page.navigate()
        logger.info(f"Открыта страница: {page.url}")
        
        login_page.login(TestConfig.STANDARD_USER, TestConfig.PASSWORD)
        logger.info(f"Выполнен вход пользователем: {TestConfig.STANDARD_USER}")
        
        # Проверка успешной авторизации
        assert inventory_page.is_inventory_displayed(), "Страница с товарами не отображается после авторизации"
        logger.info("Проверка успешной авторизации пройдена")
    
    def test_failed_login_locked_user(self, page):
        """
        Тест неудачной авторизации заблокированным пользователем.
        """
        logger.info("Начало теста неудачной авторизации заблокированным пользователем")
        
        # Создание объекта страницы
        login_page = LoginPage(page)
        
        # Шаги теста
        login_page.navigate()
        logger.info(f"Открыта страница: {page.url}")
        
        login_page.login(TestConfig.LOCKED_USER, TestConfig.PASSWORD)
        logger.info(f"Попытка входа заблокированным пользователем: {TestConfig.LOCKED_USER}")
        
        # Проверка сообщения об ошибке
        error_message = login_page.get_error_message()
        assert error_message, "Сообщение об ошибке не отображается"
        assert "locked" in error_message.lower(), f"Неожиданное сообщение об ошибке: {error_message}"
        logger.info(f"Проверка сообщения об ошибке пройдена: {error_message}")
    
    def test_failed_login_invalid_credentials(self, page):
        """
        Тест неудачной авторизации с неверными учетными данными.
        """
        logger.info("Начало теста неудачной авторизации с неверными учетными данными")
        
        # Создание объекта страницы
        login_page = LoginPage(page)
        
        # Шаги теста
        login_page.navigate()
        logger.info(f"Открыта страница: {page.url}")
        
        login_page.login("invalid_user", "invalid_password")
        logger.info("Попытка входа с неверными учетными данными")
        
        # Проверка сообщения об ошибке
        error_message = login_page.get_error_message()
        assert error_message, "Сообщение об ошибке не отображается"
        assert "username and password" in error_message.lower(), f"Неожиданное сообщение об ошибке: {error_message}"
        logger.info(f"Проверка сообщения об ошибке пройдена: {error_message}")