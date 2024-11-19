import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure the logs/ directory exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Logger setup
logger = logging.getLogger("riskasaservice")
logger.setLevel(logging.DEBUG)

# Handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    os.path.join(log_dir, "app.log"), maxBytes=1000000, backupCount=3
)

# Formatters
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
