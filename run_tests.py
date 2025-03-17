import os
import subprocess
import pytest
import argparse
from datetime import datetime

def run_tests(browser="chromium", headless=False, slow_mo=None, video=False, html_report=True, tests_path="tests"):
    """
    Запуск тестов с заданными параметрами.
    
    :param browser: браузер для запуска тестов (chromium, firefox, webkit)
    :param headless: запуск в режиме без графического интерфейса
    :param slow_mo: задержка между действиями в миллисекундах
    :param video: запись видео во время выполнения тестов
    :param html_report: генерация HTML-отчета
    :param tests_path: путь к директории с тестами
    """
    # Создание директорий для отчетов
    os.makedirs("reports/screenshots", exist_ok=True)
    if video:
        os.makedirs("reports/videos", exist_ok=True)
    
    # Формирование аргументов командной строки
    cmd = [
        "pytest",
        tests_path,
        f"--browser={browser}",
    ]
    
    # Добавление опции для запуска в headless режиме
    if headless:
        cmd.append("--headless")
    
    # Добавление опции для замедления действий
    if slow_mo is not None:
        cmd.append(f"--slowmo={slow_mo}")
    
    # Добавление опции для записи видео
    if video:
        cmd.append("--video=on")
    
    # Добавление опции для генерации HTML-отчета
    if html_report:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"reports/report_{timestamp}.html"
        cmd.append(f"--html={report_name}")
    
    # Запуск тестов
    subprocess.run(cmd)

if __name__ == "__main__":
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description="Запуск автоматизированных тестов с Playwright")
    parser.add_argument("--browser", choices=["chromium", "firefox", "webkit"], default="chromium",
                        help="Браузер для запуска тестов")
    parser.add_argument("--headless", action="store_true", help="Запуск в режиме без графического интерфейса")
    parser.add_argument("--slow-mo", type=int, help="Задержка между действиями в миллисекундах")
    parser.add_argument("--video", action="store_true", help="Запись видео во время выполнения тестов")
    parser.add_argument("--no-html", action="store_true", help="Отключение генерации HTML-отчета")
    parser.add_argument("--tests-path", default="tests", help="Путь к директории с тестами")
    
    args = parser.parse_args()
    
    run_tests(
        browser=args.browser,
        headless=args.headless,
        slow_mo=args.slow_mo,
        video=args.video,
        html_report=not args.no_html,
        tests_path=args.tests_path
    )