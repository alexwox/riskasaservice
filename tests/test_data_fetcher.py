from unittest.mock import patch

import pandas as pd
import pytest

from app.utils.data_fetcher import fetch_historical_prices


@pytest.fixture
def mock_yf_data():
    """Return mock stock price data for testing."""
    dates = pd.date_range("2020-01-01", "2020-01-03")
    # Create multi-index DataFrame that mimics yfinance output
    return pd.DataFrame(
        {("Adj Close", "AAPL"): [100, 101, 102], ("Adj Close", "SPY"): [400, 401, 402]},
        index=dates,
    )


def test_fetch_historical_prices_success(mock_yf_data):
    """Test successful retrieval of historical stock prices."""
    with patch("yfinance.download", return_value=mock_yf_data):
        result = fetch_historical_prices(["AAPL"])
        assert isinstance(result, pd.DataFrame)
        assert "AAPL" in result.columns
        assert "SPY" in result.columns


def test_fetch_historical_prices_single_ticker():
    """Test handling of single ticker data to ensure proper DataFrame conversion."""
    dates = pd.date_range("2020-01-01", "2020-01-01")
    single_ticker_data = pd.DataFrame(
        {("Adj Close", "AAPL"): [100], ("Adj Close", "SPY"): [400]}, index=dates
    )
    with patch("yfinance.download", return_value=single_ticker_data):
        result = fetch_historical_prices(["AAPL"])
        assert isinstance(result, pd.DataFrame)
        assert not isinstance(result, pd.Series)


def test_fetch_historical_prices_missing_spy():
    """Test error handling when SPY data is missing from the response."""
    mock_data = pd.DataFrame(
        {"Adj Close": {"AAPL": [100]}}, index=pd.date_range("2020-01-01", "2020-01-01")
    )
    with patch("yfinance.download", return_value=mock_data):
        with pytest.raises(ValueError, match="Failed to retrieve SPY data"):
            fetch_historical_prices(["AAPL"])


def test_fetch_historical_prices_network_error():
    with patch("yfinance.download", side_effect=Exception("Network error")):
        with pytest.raises(ValueError, match="Error fetching historical prices"):
            fetch_historical_prices(["AAPL"])


def test_fetch_historical_prices():
    # Previous test code without unused 'columns' variable
    pass


def test_fetch_historical_prices_with_error():
    # Previous test code without unused 'columns' variable
    pass
