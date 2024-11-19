"""Financial metrics calculation module for portfolio analysis and risk assessment."""

import numpy as np
from scipy import stats

from app.utils.data_fetcher import fetch_historical_prices


def calculate_portfolio_weights(portfolio):
    """Calculate portfolio weights based on quantities."""
    if not portfolio:
        raise ValueError("Portfolio cannot be empty.")
    quantities = np.array(list(portfolio.values()))
    total_investment = sum(quantities)
    return quantities / total_investment, total_investment


def calculate_historical_var(returns, weights, confidence_level=5):
    """Calculate historical Value at Risk (VaR)."""
    portfolio_returns = returns.dot(weights)
    return np.percentile(portfolio_returns, confidence_level), portfolio_returns


def calculate_parametric_var(
    portfolio_returns, total_investment, confidence_level=0.05
):
    """Calculate parametric VaR using a t-distribution."""
    t_params = stats.t.fit(portfolio_returns)
    t_var = stats.t.ppf(confidence_level, *t_params) * np.std(
        portfolio_returns
    ) + np.mean(portfolio_returns)
    return t_var * total_investment


def calculate_beta(portfolio_returns, spy_returns):
    """Calculate beta of the portfolio relative to SPY."""
    spy_variance = np.var(spy_returns)
    if spy_variance == 0:
        raise ValueError("Variance of SPY returns cannot be zero.")
    return np.cov(portfolio_returns, spy_returns)[0, 1] / spy_variance


def calculate_diversification_score(returns):
    """Calculate diversification score based on correlation."""
    correlation_matrix = returns.corr()
    return 1 - correlation_matrix.mean().mean()


def calculate_risk_metrics(portfolio):
    """Main function to calculate all risk metrics for a given portfolio."""
    tickers = list(portfolio.keys())
    historical_prices = fetch_historical_prices(tickers + ["SPY"])

    # Separate SPY from the rest of the data
    stock_data = historical_prices.drop(columns=["SPY"])
    spy_data = historical_prices["SPY"]

    # Calculate portfolio weights
    weights, total_investment = calculate_portfolio_weights(portfolio)

    # Calculate returns
    returns = stock_data.pct_change().dropna()
    spy_returns = spy_data.pct_change().dropna()

    # Calculate Historical VaR
    hist_var_95, portfolio_returns = calculate_historical_var(returns, weights)

    # Calculate Parametric VaR
    param_var_95 = calculate_parametric_var(portfolio_returns, total_investment)

    # Calculate Beta
    beta = calculate_beta(portfolio_returns, spy_returns)

    # Calculate Diversification Score
    diversification_score = calculate_diversification_score(returns)

    # Return results
    return {
        "historical_var_95": round(hist_var_95 * total_investment, 2),
        "parametric_var_95": round(param_var_95, 2),
        "beta": round(beta, 2),
        "diversification_score": round(diversification_score, 2),
    }
