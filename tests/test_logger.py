"""Test module for logging functionality."""

import logging
import os

from app.utils.logger import logger


# Set up a test logger to capture outputs
def test_logger_basic_usage():
    """Test basic logging at different levels."""
    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")
    print("Basic logging test completed.")


def test_logger_dynamic_level():
    """Test dynamically setting log levels."""
    # Change log level to WARNING
    logger.setLevel(logging.WARNING)

    # Log messages of different levels
    logger.debug("DEBUG message - Should not appear.")
    logger.info("INFO message - Should not appear.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
    logger.critical("This is a CRITICAL message.")
    print("Dynamic log level test completed.")


def test_logger_to_file():
    """Test logging to a file."""
    log_file = "test.log"

    # Add a temporary file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    logger.addHandler(file_handler)

    # Log messages
    logger.info("This should appear in the log file.")
    logger.error("An error message in the log file.")

    # Remove the file handler after test
    logger.removeHandler(file_handler)

    # Verify log file content (optional)
    if os.path.exists(log_file):
        print(f"Log file '{log_file}' created successfully. Check its content.")
        os.remove(log_file)
    else:
        print("Log file test failed.")


# Run all tests
if __name__ == "__main__":
    print("Starting logger tests...")
    test_logger_basic_usage()
    test_logger_dynamic_level()
    test_logger_to_file()
    print("All logger tests completed.")
