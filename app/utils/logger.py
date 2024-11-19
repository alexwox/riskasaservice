import logging
from logging.handlers import RotatingFileHandler

# Create a custom logger
logger = logging.getLogger("riskasaservice")
logger.setLevel(logging.DEBUG)  # Set the minimum log level (e.g., DEBUG, INFO)

# Create handlers
console_handler = logging.StreamHandler()  # Logs to console
file_handler = RotatingFileHandler(
    "logs/app.log", maxBytes=1000000, backupCount=3
)  # Logs to file with rotation

# Set log levels for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)  # Include timestamp, name, and level

# Add formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)