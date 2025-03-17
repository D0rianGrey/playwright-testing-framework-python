from page_objects.base_page import BasePage

class InventoryPage(BasePage):
    """
    Класс, представляющий страницу с товарами.
    """
    
    # Селекторы элементов страницы
    __inventory_container = "#inventory_container"
    __menu_button = "#react-burger-menu-btn"
    __logout_link = "#logout_sidebar_link"
    __shopping_cart = ".shopping_cart_link"
    __product_item = ".inventory_item"
    __add_to_cart_button = "button[id^='add-to-cart']"
    __remove_button = "button[id^='remove']"
    
    def navigate(self):
        """
        Переход на страницу с товарами.
        """
        super().navigate("/inventory.html")
    
    def is_inventory_displayed(self):
        """
        Проверка отображения списка товаров.
        :return: True, если список товаров отображается, иначе False
        """
        return self.is_element_visible(self.__inventory_container)
    
    def open_menu(self):
        """
        Открытие бокового меню.
        """
        self.click(self.__menu_button)
    
    def logout(self):
        """
        Выход из системы.
        """
        self.open_menu()
        self.wait_for_selector(self.__logout_link).click()
    
    def get_products_count(self):
        """
        Получение количества товаров на странице.
        :return: количество товаров
        """
        return len(self.page.query_selector_all(self.__product_item))
    
    def add_product_to_cart(self, index=0):
        """
        Добавление товара в корзину по индексу.
        :param index: индекс товара (начиная с 0)
        """
        add_buttons = self.page.query_selector_all(self.__add_to_cart_button)
        if 0 <= index < len(add_buttons):
            add_buttons[index].click()
        else:
            raise IndexError(f"Индекс {index} выходит за пределы доступных товаров")
    
    def remove_product_from_cart(self, index=0):
        """
        Удаление товара из корзины по индексу.
        :param index: индекс товара (начиная с 0)
        """
        remove_buttons = self.page.query_selector_all(self.__remove_button)
        if 0 <= index < len(remove_buttons):
            remove_buttons[index].click()
        else:
            raise IndexError(f"Индекс {index} выходит за пределы товаров в корзине")
    
    def open_cart(self):
        """
        Открытие корзины.
        """
        self.click(self.__shopping_cart)