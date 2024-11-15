from fastapi import APIRouter, HTTPException
from app.services.financial_metrics import calculate_risk_metrics
from app.models.portfolio import PortfolioRequest, PortfolioResponse

router = APIRouter(prefix="/portfolio", tags=["Portfolio Analysis"])

@router.post("/analyze", response_model=PortfolioResponse)
async def analyze_portfolio(portfolio: PortfolioRequest):
    """
    Analyze a portfolio and calculate risk metrics.

    ## Description
    This endpoint calculates various risk metrics for a given portfolio of stocks:
    * Value at Risk (VaR) at 95% confidence level
    * Portfolio Beta against S&P 500
    * Diversification score

    ## Parameters
    - portfolio: Dictionary of stock tickers and their quantities

    ## Returns
    - Risk metrics including VaR, Beta, and diversification score

    ## Example
    ```python
    {
        "holdings": {
            "AAPL": 10,
            "GOOG": 5,
            "MSFT": 15
        }
    }
    ```
    """
    try:
        results = calculate_risk_metrics(portfolio.holdings)
        return {"risk_metrics": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/health")
async def health():
    """
    Check the health status of the portfolio analysis service.
    
    Returns:
        dict: Status message indicating service health
    """
    return {"status": "ok"}