import os
from dotenv import load_dotenv
from binance.client import Client
from src.mock_client import MockClient

# Load environment variables
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
MOCK_MODE = os.getenv('MOCK_MODE', 'False').lower() in ('true', '1', 't')

def get_binance_client(testnet=True):
    """
    Initialize and return the Binance Client.
    Defaults to Testnet.
    Returns MockClient if MOCK_MODE is True or keys are missing.
    """
    if MOCK_MODE or not API_KEY or not API_SECRET or API_KEY == 'your_api_key_here':
        print("WARNING: Running in MOCK MODE. No real orders will be placed.")
        return MockClient(API_KEY, API_SECRET, testnet=testnet)
    
    return Client(API_KEY, API_SECRET, testnet=testnet)
