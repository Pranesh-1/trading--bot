import argparse
import sys
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit_order
from src.advanced.oco import place_oco_order
from src.utils import setup_logger

logger = setup_logger('main_cli')

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot CLI")
    subparsers = parser.add_subparsers(dest='command', help='Order type to execute')

    # Market Order Parser
    market_parser = subparsers.add_parser('market', help='Place a Market Order')
    market_parser.add_argument('symbol', type=str, help='Trading Symbol (e.g., BTCUSDT)')
    market_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order Side')
    market_parser.add_argument('quantity', type=float, help='Order Quantity')

    # Limit Order Parser
    limit_parser = subparsers.add_parser('limit', help='Place a Limit Order')
    limit_parser.add_argument('symbol', type=str, help='Trading Symbol')
    limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order Side')
    limit_parser.add_argument('quantity', type=float, help='Order Quantity')
    limit_parser.add_argument('price', type=float, help='Limit Price')

    # Stop-Limit Order Parser
    stop_limit_parser = subparsers.add_parser('stop_limit', help='Place a Stop-Limit Order')
    stop_limit_parser.add_argument('symbol', type=str, help='Trading Symbol')
    stop_limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order Side')
    stop_limit_parser.add_argument('quantity', type=float, help='Order Quantity')
    stop_limit_parser.add_argument('price', type=float, help='Limit Price')
    stop_limit_parser.add_argument('stop_price', type=float, help='Stop Trigger Price')

    # OCO Order Parser
    oco_parser = subparsers.add_parser('oco', help='Place an OCO Order Strategy')
    oco_parser.add_argument('symbol', type=str, help='Trading Symbol')
    oco_parser.add_argument('side', type=str, choices=['BUY', 'SELL'], help='Order Side')
    oco_parser.add_argument('quantity', type=float, help='Order Quantity')
    oco_parser.add_argument('price', type=float, help='Take Profit Limit Price')
    oco_parser.add_argument('stop_price', type=float, help='Stop Loss Trigger Price')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == 'market':
            place_market_order(args.symbol, args.side, args.quantity)
        elif args.command == 'limit':
            place_limit_order(args.symbol, args.side, args.quantity, args.price)
        elif args.command == 'stop_limit':
            place_stop_limit_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
        elif args.command == 'oco':
            place_oco_order(args.symbol, args.side, args.quantity, args.price, args.stop_price)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
