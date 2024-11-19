from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.models.portfolio import PortfolioRequest, PortfolioResponse
from app.services.financial_metrics import calculate_risk_metrics

router = APIRouter(prefix="/portfolio", tags=["Portfolio Analysis"])


@router.post(
    "/analyze",
    response_model=PortfolioResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Successfully analyzed portfolio"},
        400: {"description": "Invalid portfolio data"},
        500: {"description": "Internal server error"},
    },
)
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
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred",
        ) from e


@router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Service is healthy"},
        503: {"description": "Service is unhealthy"},
    },
)
async def health():
    """
    Check the health status of the portfolio analysis service.

    Returns:
        dict: Status message indicating service health
    """
    try:
        # Add any health checks here if needed
        return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content={"status": "error"}
        )
