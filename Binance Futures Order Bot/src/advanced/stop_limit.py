from binance.enums import SIDE_BUY, SIDE_SELL, FUTURE_ORDER_TYPE_STOP, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException
from src.config import get_binance_client
from src.utils import setup_logger, validate_quantity, validate_price

logger = setup_logger('stop_limit_orders')

def place_stop_limit_order(symbol, side, quantity, price, stop_price):
    """
    Place a Stop-Limit order on Binance Futures.
    
    Args:
        symbol (str): Trading symbol (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Amount to trade
        price (float): Limit price
        stop_price (float): Stop trigger price
    """
    client = get_binance_client()
    
    # Validation
    is_valid_qty, qty_or_msg = validate_quantity(quantity)
    if not is_valid_qty:
        logger.error(f"Validation failed: {qty_or_msg}")
        return

    is_valid_price, price_or_msg = validate_price(price)
    if not is_valid_price:
        logger.error(f"Validation failed: {price_or_msg}")
        return

    is_valid_stop, stop_or_msg = validate_price(stop_price)
    if not is_valid_stop:
        logger.error(f"Validation failed: {stop_or_msg}")
        return
    
    side = side.upper()
    if side not in [SIDE_BUY, SIDE_SELL]:
        logger.error(f"Invalid side: {side}. Must be BUY or SELL.")
        return

    try:
        logger.info(f"Placing STOP-LIMIT {side} order for {qty_or_msg} {symbol} at {price_or_msg} (Stop: {stop_or_msg})...")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_STOP,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=qty_or_msg,
            price=price_or_msg,
            stopPrice=stop_or_msg
        )
        logger.info(f"Order placed successfully: {order}")
        return order
    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
