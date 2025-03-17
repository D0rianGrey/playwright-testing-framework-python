from page_objects.base_page import BasePage

class LoginPage(BasePage):
    """
    Класс, представляющий страницу входа в систему.
    """
    
    # Селекторы элементов страницы
    __username_input = "#user-name"
    __password_input = "#password"
    __login_button = "#login-button"
    __error_message = "h3[data-test='error']"
    
    def navigate(self):
        """
        Переход на страницу входа.
        """
        super().navigate("/")
    
    def login(self, username, password):
        """
        Выполнение входа в систему.
        :param username: имя пользователя
        :param password: пароль
        """
        self.fill(self.__username_input, username)
        self.fill(self.__password_input, password)
        self.click(self.__login_button)
    
    def get_error_message(self):
        """
        Получение текста сообщения об ошибке.
        :return: текст сообщения об ошибке или None, если сообщения нет
        """
        error_element = self.page.query_selector(self.__error_message)
        if error_element:
            return error_element.text_content()
        return None
    
    def is_login_button_visible(self):
        """
        Проверка видимости кнопки входа.
        :return: True, если кнопка видна, иначе False
        """
        return self.is_element_visible(self.__login_button)