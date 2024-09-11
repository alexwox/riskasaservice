from fastapi import FastAPI
from pydantic import BaseModel
import yfinance as yf
import numpy as np
import pandas as pd
from scipy import stats

app = FastAPI()

class Portfolio(BaseModel):
    tickers: list[str]
    weights: list[float]

@app.post("/t_distribution")
async def fit_t_distribution(portfolio: Portfolio):
    tickers = portfolio.tickers
    data = yf.download(tickers, period='1y')['Adj Close']

    # Handle single ticker case
    if isinstance(data, pd.Series):
        data = data.to_frame()

    # Calculate log returns
    log_returns = np.log(data / data.shift(1)).dropna()

    t_dist_params = {}
    for ticker in tickers:
        # Fit t-distribution to log returns
        params = stats.t.fit(log_returns[ticker])
        t_dist_params[ticker] = {
            "df": params[0],
            "loc": params[1],
            "scale": params[2]
        }

    return t_dist_params

# Refactor the sharpe ratio calculation to reuse data download
def download_data(tickers):
    data = yf.download(tickers, period='1y')['Adj Close']
    if isinstance(data, pd.Series):
        data = data.to_frame()
    return data

def calculate_returns(data):
    return data.pct_change().dropna()

@app.post("/sharpe_ratio")
async def calculate_sharpe(portfolio: Portfolio):
    tickers = portfolio.tickers
    weights = portfolio.weights
    data = download_data(tickers)
    returns = calculate_returns(data)

    # Calculate portfolio returns
    portfolio_returns = (returns * weights).sum(axis=1)
    
    # Calculate Sharpe ratio: (mean return / standard deviation of returns)
    sharpe_ratio = portfolio_returns.mean() / portfolio_returns.std() * np.sqrt(252)  # Annualized Sharpe
    
    return {"sharpe_ratio": sharpe_ratio}

