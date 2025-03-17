from utils.logger import Logger
import os
import sys
import pytest
from playwright.sync_api import sync_playwright

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Настройка логгера
logger = Logger.setup_logger()


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """
    Фикстура для настройки аргументов запуска браузера.
    """
    return {
        "headless": False,  # Для отладки - браузер будет видимым
        "slow_mo": 100,     # Замедление операций для отладки
    }


@pytest.fixture(scope="session")
def browser_context_args():
    """
    Фикстура для настройки контекста браузера.
    """
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "record_video_dir": "reports/videos",  # Директория для записи видео
    }


@pytest.fixture(scope="function")
def page(browser):
    """
    Фикстура для создания страницы браузера.
    Scope="function" означает, что новая страница будет создаваться для каждого теста.
    """
    page = browser.new_page()
    logger.info(f"Создана новая страница браузера")

    # Действия до теста
    yield page

    # Действия после теста
    logger.info(f"Тест завершен, закрытие страницы")
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншота при ошибке в тесте.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                # Создание скриншота при падении теста
                screenshot_path = f"reports/screenshots/{item.name}_{call.start:.0f}.png"
                page.screenshot(path=screenshot_path)
                logger.info(f"Скриншот сохранен: {screenshot_path}")
        except Exception as e:
            logger.error(f"Ошибка при создании скриншота: {str(e)}")
