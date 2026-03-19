from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="{time} | {level} | {message} | {extra}",
    level="INFO"
)

logger.add(
    "logs/app.log",
    rotation="50 MB",
    level="INFO",
    format="{time} | {level} | {name}:{function}:{line} | {message} | {extra}",
)