import yfinance as yf
import numpy as np
from scipy import stats
import pandas as pd
from app.schemas.portfolio import Portfolio

def download_data(tickers):
    data = yf.download(tickers, period='1y')['Adj Close']
    if isinstance(data, pd.Series):
        data = data.to_frame()
    return data

def calculate_log_returns(data):
    return np.log(data / data.shift(1)).dropna()

def fit_t_distribution(portfolio: Portfolio):
    tickers = portfolio.tickers
    data = download_data(tickers)
    log_returns = calculate_log_returns(data)

    t_dist_params = {}
    for ticker in tickers:
        params = stats.t.fit(log_returns[ticker])
        t_dist_params[ticker] = {
            "df": params[0],
            "loc": params[1],
            "scale": params[2]
        }
    return t_dist_params

def calculate_sharpe_ratio(portfolio: Portfolio):
    tickers = portfolio.tickers
    weights = portfolio.weights
    data = download_data(tickers)
    returns = calculate_log_returns(data).pct_change().dropna()

    portfolio_returns = (returns * weights).sum(axis=1)
    sharpe_ratio = portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(252)
    return sharpe_ratio

def calculate_var(portfolio: Portfolio, confidence_level=0.95):
    tickers = portfolio.tickers
    data = download_data(tickers)
    log_returns = calculate_log_returns(data)

    var = {}
    for ticker in tickers:
        var[ticker] = np.percentile(log_returns[ticker], (1 - confidence_level) * 100)
    return var

def calculate_cvar(portfolio: Portfolio, confidence_level=0.95):
    tickers = portfolio.tickers
    data = download_data(tickers)
    log_returns = calculate_log_returns(data)

    cvar = {}
    for ticker in tickers:
        var_value = np.percentile(log_returns[ticker], (1 - confidence_level) * 100)
        cvar[ticker] = log_returns[ticker][log_returns[ticker] <= var_value].mean()
    return cvar