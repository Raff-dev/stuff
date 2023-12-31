# filename: stock_ytd_gain.py

import yfinance as yf
import datetime

# Define the start date as the first day of the current year
start_date = datetime.date(datetime.date.today().year, 1, 1)

# Define the end date as today
end_date = datetime.date.today()

# Define the ticker symbols
tickers = ['META', 'TSLA']

# Fetch the data
data = yf.download(tickers, start=start_date, end=end_date)

# Calculate and print the YTD gain for each stock
for ticker in tickers:
    ytd_gain = (data['Close'][ticker][-1] - data['Close'][ticker][0]) / data['Close'][ticker][0] * 100
    print(f"The YTD gain for {ticker} is {ytd_gain}%")