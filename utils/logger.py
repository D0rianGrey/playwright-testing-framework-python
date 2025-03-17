import logging
import os
from datetime import datetime


class Logger:
    """
    Класс для настройки и использования логирования в проекте.
    """

    @staticmethod
    def setup_logger(name="automation", level=logging.INFO):
        """
        Настройка логгера.
        :param name: имя логгера
        :param level: уровень логирования
        :return: настроенный логгер
        """
        # Создание директории для логов, если она не существует
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Формирование имени файла лога с датой
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"{name}_{timestamp}.log")

        # Настройка логгера
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Удаление существующих обработчиков, если они есть
        if logger.handlers:
            logger.handlers.clear()

        # Обработчик для записи в файл
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_format)
        file_handler.setLevel(level)

        # Обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(file_format)
        console_handler.setLevel(level)

        # Добавление обработчиков к логгеру
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.info(f"Логирование настроено. Файл лога: {log_file}")

        return logger
