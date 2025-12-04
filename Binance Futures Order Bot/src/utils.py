import logging
import sys

def setup_logger(name='bot_logger', log_file='bot.log', level=logging.INFO):
    """
    Setup a logger that writes to both a file and the console.
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def validate_quantity(quantity):
    """
    Validate that quantity is a positive number.
    """
    try:
        qty = float(quantity)
        if qty <= 0:
            return False, "Quantity must be positive."
        return True, qty
    except ValueError:
        return False, "Quantity must be a valid number."

def validate_price(price):
    """
    Validate that price is a positive number.
    """
    try:
        p = float(price)
        if p <= 0:
            return False, "Price must be positive."
        return True, p
    except ValueError:
        return False, "Price must be a valid number."
