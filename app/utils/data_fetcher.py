import pandas as pd
import yfinance as yf


def fetch_historical_prices(tickers, start_date="2020-01-01", end_date="2023-01-01"):
    # Ensure SPY is included for market benchmark data
    if "SPY" not in tickers:
        tickers.append("SPY")

    # Attempt to fetch data
    try:
        data = yf.download(tickers, start=start_date, end=end_date)["Adj Close"]
        if isinstance(data, pd.Series):  # Single ticker case
            data = data.to_frame()

        # Check if SPY is included in the data
        if "SPY" not in data.columns:
            raise ValueError(
                "Failed to retrieve SPY data. Please check your internet connection."
            )

        return data
    except Exception as e:
        raise ValueError(f"Error fetching historical prices: {e}")
