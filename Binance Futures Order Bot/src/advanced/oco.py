from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_LIMIT, FUTURE_ORDER_TYPE_STOP_MARKET, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException
from src.config import get_binance_client
from src.utils import setup_logger, validate_quantity, validate_price

logger = setup_logger('oco_orders')

def place_oco_order(symbol, side, quantity, price, stop_price):
    """
    Place an OCO (One-Cancels-the-Other) order strategy.
    Note: Binance Futures API does not support native OCO orders like Spot.
    This implementation places two separate orders: a Limit (Take Profit) and a Stop Market (Stop Loss).
    WARNING: This is a basic simulation and does not automatically cancel the other order when one fills.
    
    Args:
        symbol (str): Trading symbol (e.g., 'BTCUSDT')
        side (str): 'BUY' or 'SELL'
        quantity (float): Amount to trade
        price (float): Take Profit Limit price
        stop_price (float): Stop Loss trigger price
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

    # Determine opposite side for closing position if this was intended to close an open position,
    # but typically OCO is for opening or closing. Assuming this is for opening 2 conditional orders?
    # Actually, OCO is usually: Limit Maker (Take Profit) AND Stop Loss.
    # If side is BUY (Long), TP is Sell Limit > Current, SL is Sell Stop < Current.
    # If side is SELL (Short), TP is Buy Limit < Current, SL is Buy Stop > Current.
    
    # For simplicity in this assignment, we will place a LIMIT order and a STOP_MARKET order.
    # NOTE: In a real bot, we'd need a websocket listener to cancel the other order.
    
    try:
        logger.info(f"Placing OCO strategy for {symbol}...")
        
        # 1. Place Limit Order (Take Profit)
        logger.info(f"Placing Limit Order (TP) at {price_or_msg}...")
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=qty_or_msg,
            price=price_or_msg
        )
        logger.info(f"TP Order placed: {tp_order['orderId']}")

        # 2. Place Stop Market Order (Stop Loss)
        logger.info(f"Placing Stop Market Order (SL) at {stop_or_msg}...")
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_STOP_MARKET,
            quantity=qty_or_msg,
            stopPrice=stop_or_msg
        )
        logger.info(f"SL Order placed: {sl_order['orderId']}")
        
        return {'tp_order': tp_order, 'sl_order': sl_order}

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: {e}")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
