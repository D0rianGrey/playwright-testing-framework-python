class TestConfig:
    # URL тестируемого приложения
    BASE_URL = "https://www.saucedemo.com"
    
    # Учетные данные для тестов
    STANDARD_USER = "standard_user"
    LOCKED_USER = "locked_out_user"
    PASSWORD = "secret_sauce"
    
    # Таймауты (в миллисекундах)
    DEFAULT_TIMEOUT = 30000
    
    # Пути к отчетам
    REPORT_PATH = "./reports"