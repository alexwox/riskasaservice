from app.services.portfolio import calculate_sharpe_ratio
from app.schemas.portfolio import Portfolio

def test_calculate_sharpe_ratio():
    portfolio = Portfolio(tickers=["AAPL", "GOOG"], weights=[0.4, 0.6])
    result = calculate_sharpe_ratio(portfolio)
    assert result["sharpe_ratio"] is not None