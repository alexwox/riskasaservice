import numpy as np
import pandas as pd
from app.utils.data_fetcher import fetch_historical_prices

import numpy as np
from app.utils.data_fetcher import fetch_historical_prices

def calculate_risk_metrics(portfolio):
    tickers = list(portfolio.keys())
    historical_prices = fetch_historical_prices(tickers + ["SPY"])
    
    # Separate SPY from the rest of the data
    stock_data = historical_prices.drop(columns=["SPY"])
    spy_data = historical_prices["SPY"]

    # Calculate returns for portfolio stocks
    returns = stock_data.pct_change().dropna()

    # Portfolio weights
    quantities = np.array(list(portfolio.values()))
    total_investment = sum(quantities)
    weights = quantities / total_investment

    # Value at Risk (VaR)
    portfolio_returns = returns.dot(weights)
    var_95 = np.percentile(portfolio_returns, 5) * total_investment

    # Beta calculation using SPY data as the market benchmark
    spy_returns = spy_data.pct_change().dropna()
    beta = np.cov(portfolio_returns, spy_returns)[0, 1] / np.var(spy_returns)

    # Diversification score
    correlation_matrix = returns.corr()
    diversification_score = 1 - correlation_matrix.mean().mean()

    return {
        "value_at_risk_95": round(var_95, 2),
        "beta": round(beta, 2),
        "diversification_score": round(diversification_score, 2),
    }