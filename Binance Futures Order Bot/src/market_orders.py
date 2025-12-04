from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET
from binance.exceptions import BinanceAPIException
from src.config import get_binance_client
from src.utils import setup_logger, validate_quantity

logger = setup_logger('market_orders')

def place_market_order(symbol, side, quantity):
    """
    Place a market order on Binance Futures.
    
    Args:
        symbol (str): Trading symbol (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Amount to trade
    """
    client = get_binance_client()
    
    # Validation
    is_valid_qty, qty_or_msg = validate_quantity(quantity)
    if not is_valid_qty:
        logger.error(f"Validation failed: {qty_or_msg}")
        return
    
    side = side.upper()
    if side not in [SIDE_BUY, SIDE_SELL]:
        logger.error(f"Invalid side: {side}. Must be BUY or SELL.")
        return

    try:
        logger.info(f"Placing MARKET {side} order for {qty_or_msg} {symbol}...")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=qty_or_msg
        )
        logger.info(f"Order placed successfully: {order}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
