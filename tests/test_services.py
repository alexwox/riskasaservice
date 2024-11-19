from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from app.services.financial_metrics import (
    calculate_beta,
    calculate_diversification_score,
    calculate_historical_var,
    calculate_portfolio_weights,
    calculate_risk_metrics,
)


def test_calculate_portfolio_weights():
    """Test portfolio weights calculation."""
    portfolio = {"AAPL": 5, "GOOG": 10}
    weights, total = calculate_portfolio_weights(portfolio)
    assert total == 15
    assert np.isclose(weights[0], 5 / 15)
    assert np.isclose(weights[1], 10 / 15)

    # Test edge case: empty portfolio
    with pytest.raises(ValueError, match="Portfolio cannot be empty."):
        calculate_portfolio_weights({})


def test_calculate_beta():
    """Test beta calculation."""
    portfolio_returns = pd.Series([0.01, 0.02, -0.01, 0.005])
    spy_returns = pd.Series([0.02, 0.01, -0.005, 0.01])
    beta = calculate_beta(portfolio_returns, spy_returns)
    assert beta > 0  # Example: beta should be positive

    # Test edge case: zero variance in SPY
    spy_returns = pd.Series([0.02, 0.02, 0.02, 0.02])
    with pytest.raises(ValueError, match="Variance of SPY returns cannot be zero."):
        calculate_beta(portfolio_returns, spy_returns)


def test_calculate_historical_var():
    """Test historical VaR calculation."""
    returns = pd.DataFrame({"AAPL": [0.01, 0.02, -0.01], "GOOG": [0.03, -0.02, 0.01]})
    weights = np.array([0.6, 0.4])
    hist_var, _ = calculate_historical_var(returns, weights)
    assert hist_var < 0  # Historical VaR should be negative for risk assessment

    # Test edge case: empty returns
    with pytest.raises(ValueError):
        calculate_historical_var(pd.DataFrame(), weights)


def test_calculate_diversification_score():
    """Test diversification score calculation."""
    returns = pd.DataFrame(
        {"AAPL": [0.01, 0.02, -0.01, 0.005, 0], "GOOG": [0.03, -0.02, 0.01, 0.005, 0]}
    )
    score = calculate_diversification_score(returns)
    assert 0 <= score <= 1

    # Test edge case: single stock (no diversification)
    returns = pd.DataFrame({"AAPL": [0.01, 0.02, -0.01]})
    score = calculate_diversification_score(returns)
    assert score == 0


@patch("app.services.financial_metrics.fetch_historical_prices")
def test_calculate_risk_metrics(mock_fetch_historical_prices):
    """Test full risk metrics calculation with mocked data."""
    # Mock the historical prices
    mock_fetch_historical_prices.return_value = pd.DataFrame(
        {
            "AAPL": [150, 152, 151, 153, 154],
            "GOOG": [2800, 2820, 2810, 2840, 2800],
            "SPY": [400, 402, 401, 403, 404],
        }
    )

    # Test a sample portfolio
    portfolio = {"AAPL": 5, "GOOG": 10}
    result = calculate_risk_metrics(portfolio)

    # Assert intermediate values
    assert result["historical_var_95"] is not None
    assert result["beta"] is not None
    assert result["diversification_score"] is not None

    # Assert values are finite numbers
    for key, value in result.items():
        print(f"{key}: {value}")
        assert np.isfinite(value)
