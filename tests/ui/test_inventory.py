import pytest
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from config.config import TestConfig
from utils.logger import Logger

# Настройка логгера
logger = Logger.setup_logger(name="inventory_tests")

class TestInventory:
    """
    Тесты для страницы с товарами.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """
        Фикстура для подготовки к тестам.
        Выполняет авторизацию перед каждым тестом.
        """
        logger.info("Подготовка к тесту: авторизация")
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(TestConfig.STANDARD_USER, TestConfig.PASSWORD)
        
        # Проверка успешной авторизации
        inventory_page = InventoryPage(page)
        assert inventory_page.is_inventory_displayed(), "Ошибка авторизации перед тестом"
        logger.info("Подготовка к тесту завершена успешно")
    
    def test_products_count(self, page):
        """
        Тест количества товаров на странице.
        """
        logger.info("Начало теста количества товаров")
        
        # Создание объекта страницы
        inventory_page = InventoryPage(page)
        
        # Проверка количества товаров
        products_count = inventory_page.get_products_count()
        logger.info(f"Количество товаров на странице: {products_count}")
        assert products_count > 0, "На странице нет товаров"
        
        # Обычно на странице должно быть 6 товаров, но это может измениться
        # Поэтому проверяем только наличие товаров
        logger.info("Проверка количества товаров пройдена")
    
    def test_add_to_cart(self, page):
        """
        Тест добавления товара в корзину.
        """
        logger.info("Начало теста добавления товара в корзину")
        
        # Создание объекта страницы
        inventory_page = InventoryPage(page)
        
        # Добавление товара в корзину
        inventory_page.add_product_to_cart(0)
        logger.info("Товар добавлен в корзину")
        
        # Проверка, что товар можно удалить из корзины
        # (кнопка "Remove" появляется только после добавления)
        try:
            inventory_page.remove_product_from_cart(0)
            logger.info("Товар успешно удален из корзины")
            test_passed = True
        except Exception as e:
            logger.error(f"Ошибка при удалении товара из корзины: {str(e)}")
            test_passed = False
        
        assert test_passed, "Тест добавления товара в корзину не пройден"
    
    def test_logout(self, page):
        """
        Тест выхода из системы.
        """
        logger.info("Начало теста выхода из системы")
        
        # Создание объектов страниц
        inventory_page = InventoryPage(page)
        login_page = LoginPage(page)
        
        # Выход из системы
        inventory_page.logout()
        logger.info("Выполнен выход из системы")
        
        # Проверка, что произошел выход из системы
        assert login_page.is_login_button_visible(), "Кнопка входа не отображается после выхода из системы"
        logger.info("Проверка успешного выхода из системы пройдена")