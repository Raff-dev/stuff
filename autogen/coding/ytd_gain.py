# filename: ytd_gain.py

import yfinance as yf
from datetime import datetime

# List of stock tickers
tickers = ["AAPL", "GOOGL", "MSFT"]

# Get the current year
current_year = datetime.now().year

# For each ticker, download the stock data and calculate the YTD gain
for ticker in tickers:
    # Download the stock data
    stock = yf.Ticker(ticker)
    hist = stock.history(start=f"{current_year}-01-01")

    # Calculate the YTD gain
    start_price = hist["Close"][0]
    end_price = hist["Close"][-1]
    ytd_gain = (end_price - start_price) / start_price * 100

    # Print the YTD gain
    print(f"The YTD gain for {ticker} is {ytd_gain:.2f}%")