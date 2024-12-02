
import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.getcwd(), "src"))
print(os.path.join(os.getcwd(), "src"))

from textSummarizer.logging import logger

logger.info("Welcome to the our custom logging")
