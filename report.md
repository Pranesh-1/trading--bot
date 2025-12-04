# Binance Futures Order Bot - Project Report

## Overview
This project implements a CLI-based trading bot for Binance USDT-M Futures. It supports core order types (Market, Limit) and advanced strategies (Stop-Limit, OCO).

## Architecture
The project is structured for modularity and extensibility:
- **`src/main.py`**: Entry point handling CLI arguments and routing commands.
- **`src/config.py`**: Manages API credentials and client initialization.
- **`src/utils.py`**: Provides centralized logging and input validation.
- **`src/market_orders.py` & `src/limit_orders.py`**: Core order logic.
- **`src/advanced/`**: Contains advanced order types (`stop_limit.py`, `oco.py`).

## Features Implemented

### 1. Core Orders
- **Market Orders**: Executed immediately at the best available price.
- **Limit Orders**: Placed at a specific price, adding liquidity to the order book.

### 2. Advanced Orders (Bonus)
- **Stop-Limit**: Combines a stop trigger with a limit order. Useful for breakout strategies or minimizing slippage.
- **OCO (One-Cancels-the-Other)**: Implemented as a strategy placing both a Take Profit (Limit) and a Stop Loss (Stop Market) order.
  - *Note*: Since Binance Futures API doesn't support native OCO, this is a client-side simulation. In a production environment, a WebSocket listener would be needed to cancel the remaining order when one fills.

### 3. Logging & Validation
- **Logging**: All actions are logged to `bot.log` with timestamps, log levels, and messages.
- **Validation**: Quantities and prices are validated to be positive numbers before any API call is made.

## Usage Examples
(See README.md for full command list)

## Future Improvements
- **WebSocket Integration**: For real-time OCO management.
- **Grid Trading**: Implementing a grid strategy for automated scalping.
- **GUI**: A simple web or desktop interface.
