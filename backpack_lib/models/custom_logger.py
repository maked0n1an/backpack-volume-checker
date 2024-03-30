import sys
from loguru import logger

logger.remove()
logger.add(
    sys.stderr,
    format="<white>{time: DD/MM/YYYY HH:mm:ss}</white> | <level>"
    "{level: <8}</level> | <white>{message}</white>"
)
logger.add(
    "main.log",
    format="<green>{time: DD/MM/YYYY HH:mm:ss}</green> | <level>"
    "{level: <8}</level> | <white>{message}</white>"
)