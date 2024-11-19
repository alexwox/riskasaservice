import os
import logging
from logging.handlers import RotatingFileHandler

# Environment-based logging level
env = os.getenv("ENV", "development").lower()
log_level = logging.DEBUG if env == "development" else logging.INFO

# Create a custom logger
logger = logging.getLogger("riskasaservice")
logger.setLevel(log_level)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler("logs/app.log", maxBytes=1000000, backupCount=3)

# Set log levels for handlers
console_handler.setLevel(logging.DEBUG if env == "development" else logging.WARNING)
file_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)