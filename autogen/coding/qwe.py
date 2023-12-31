import requests

# Define the currencies and time period
currencies = ["GBP", "PLN", "USD"]
start_date = "2021-01-01"
end_date = "2021-12-31"

# Loop through each currency and retrieve the historical data
for currency in currencies:
    url = f"https://api.exchangerate-api.com/history/{start_date}/{end_date}/{currency}"
    response = requests.get(url)
    data = response.json()

    # Loop through each date and print the currency value
    for date, value in data["rates"].items():
        print(f"{date}: {value}")
