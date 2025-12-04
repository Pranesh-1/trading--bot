import logging
import random
import uuid

logger = logging.getLogger('mock_client')

class MockClient:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet = testnet
        logger.info("Initialized MockClient. No real orders will be placed.")

    def futures_create_order(self, **kwargs):
        """
        Simulate placing a futures order.
        Returns a mock order response.
        """
        symbol = kwargs.get('symbol')
        side = kwargs.get('side')
        order_type = kwargs.get('type')
        quantity = kwargs.get('quantity')
        price = kwargs.get('price')
        stop_price = kwargs.get('stopPrice')

        logger.info(f"MOCK ORDER: {side} {quantity} {symbol} ({order_type}) Price: {price} Stop: {stop_price}")

        # Simulate some basic validation or error probability if needed
        if quantity <= 0:
             raise Exception("MockAPIError: Quantity must be greater than 0")

        # Return a mock response structure similar to python-binance
        return {
            'clientOrderId': str(uuid.uuid4()),
            'cumQty': '0',
            'cumQuote': '0',
            'executedQty': '0',
            'orderId': random.randint(10000000, 99999999),
            'avgPrice': '0.00000',
            'origQty': str(quantity),
            'price': str(price) if price else '0',
            'reduceOnly': False,
            'side': side,
            'positionSide': 'BOTH',
            'status': 'NEW',
            'stopPrice': str(stop_price) if stop_price else '0',
            'closePosition': False,
            'symbol': symbol,
            'timeInForce': 'GTC',
            'type': order_type,
            'origType': order_type,
            'updateTime': 1234567890,
            'workingType': 'CONTRACT_PRICE',
            'priceProtect': False
        }
