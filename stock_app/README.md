# Stock Big Movers - Trading App

Find stocks that made 15% or greater moves in a single day over the last week, with 21 EMA entry points plotted.

## Features

- 📊 Scans 50+ popular stocks for big moves (15%+ in one day)
- 📈 Returns top 15 biggest movers
- 💹 Displays interactive candlestick charts
- 🎯 Shows 21 EMA (Exponential Moving Average) for entry points
- 📱 Mobile-friendly interface (works great on iPhone)

## How to Use

### Installation

```bash
cd stock_app
pip install -r requirements.txt
```

### Run the App

```bash
python app.py
```

The app will start on `http://localhost:8080`

### Access from iPhone

1. Make sure your iPhone and computer are on the same network
2. Find your computer's local IP address
3. Open Safari on your iPhone and go to: `http://YOUR_IP:8080`

## How It Works

1. **Scans Stock Universe**: Checks 50+ popular stocks (AAPL, TSLA, NVDA, etc.)
2. **Finds Big Movers**: Identifies stocks that moved 15%+ in a single day
3. **Calculates 21 EMA**: Computes the exponential moving average for entry points
4. **Displays Results**: Shows interactive charts with price action and EMA

## Trading Strategy

The app shows you:
- **Big movers**: Stocks with significant momentum
- **21 EMA**: A common entry point for pullback trades
- **Current price vs EMA**: See if the stock is near your entry level

## Customization

You can modify in `app.py`:
- `STOCK_UNIVERSE`: Add more tickers to scan
- `min_move_percent`: Change the threshold (default: 15%)
- `days_back`: Adjust the lookback period (default: 7 days)
- EMA period: Change from 21 to any period you prefer

## Requirements

- Python 3.8+
- Internet connection (for fetching stock data)
- Modern web browser (Safari, Chrome, Firefox)
