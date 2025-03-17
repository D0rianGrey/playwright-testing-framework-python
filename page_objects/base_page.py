from playwright.sync_api import Page
from config.config import TestConfig

class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы, которые могут использоваться на любой странице.
    """
    
    def __init__(self, page: Page):
        self.page = page
        self.config = TestConfig()
        self.base_url = self.config.BASE_URL
        
    def navigate(self, path=""):
        """
        Переход на указанную страницу с учетом базового URL.
        :param path: путь относительно базового URL
        """
        full_url = f"{self.base_url}{path}"
        self.page.goto(full_url)
        
    def get_title(self):
        """
        Получение заголовка страницы.
        :return: заголовок страницы
        """
        return self.page.title()
    
    def wait_for_selector(self, selector, timeout=None):
        """
        Ожидание появления элемента на странице.
        :param selector: CSS-селектор элемента
        :param timeout: таймаут в миллисекундах
        :return: локатор элемента
        """
        if timeout is None:
            timeout = self.config.DEFAULT_TIMEOUT
        
        return self.page.wait_for_selector(selector, timeout=timeout)
    
    def is_element_visible(self, selector):
        """
        Проверка видимости элемента на странице.
        :param selector: CSS-селектор элемента
        :return: True, если элемент виден, иначе False
        """
        element = self.page.query_selector(selector)
        if element:
            return element.is_visible()
        return False
    
    def click(self, selector):
        """
        Клик по элементу.
        :param selector: CSS-селектор элемента
        """
        self.page.click(selector)
    
    def fill(self, selector, value):
        """
        Заполнение поля ввода.
        :param selector: CSS-селектор элемента
        :param value: значение для ввода
        """
        self.page.fill(selector, value)