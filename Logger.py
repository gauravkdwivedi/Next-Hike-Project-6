# Import the logger library
import logging

# Configure the login system you are using
logging.basicConfig(level=logging.DEBUG, # sets the login level
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Log an exception with stack trace
try:
    # Code that might raise an exception
    result = 1 / 0
except Exception as e:
    logger.exception("An exception occurred: %s", e)