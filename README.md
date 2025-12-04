# Binance Futures Order Bot

A CLI-based trading bot for Binance USDT-M Futures.

## Features
- **Market Orders**: Buy/Sell at current market price.
- **Limit Orders**: Buy/Sell at a specific price.
- **Stop-Limit Orders**: Trigger a limit order when a stop price is reached.
- **OCO Orders**: Simulated One-Cancels-the-Other strategy (Limit TP + Stop Market SL).
- **Logging**: Comprehensive logging to `bot.log` and console.
- **Validation**: Input validation for quantity and prices.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**:
   - Rename `.env.example` to `.env`.
   - Add your Binance Testnet API Key and Secret to `.env`.

   ```env
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_api_secret
   MOCK_MODE=True  # Set to True to run without real keys
   ```

   *Note: If you do not provide keys, the bot will automatically default to Mock Mode.*

## Usage

Run the bot using `python -m src.main` from the project root.

### Market Order
```bash
python -m src.main market BTCUSDT BUY 0.002
```

### Limit Order
```bash
python -m src.main limit BTCUSDT SELL 0.002 50000
```

### Stop-Limit Order
```bash
python -m src.main stop_limit BTCUSDT BUY 0.002 50000 49000
```
*Places a Buy Limit order at 50,000 when the price hits 49,000.*

### OCO Order
```bash
python -m src.main oco BTCUSDT BUY 0.002 55000 45000
```
*Places a Take Profit Limit at 55,000 and a Stop Loss Market at 45,000.*

## File Structure
- `src/`: Source code.
- `src/advanced/`: Advanced order implementations.
- `bot.log`: Log file.
