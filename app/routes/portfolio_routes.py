from fastapi import APIRouter, HTTPException
from app.services.financial_metrics import calculate_risk_metrics

router = APIRouter(prefix="/portfolio", tags=["Portfolio Analysis"])

@router.post("/analyze")
def analyze_portfolio(portfolio: dict):
    """
    Analyze the portfolio and return risk metrics.
    Portfolio format: {"AAPL": 10, "GOOG": 5, "MSFT": 15}
    """
    try:
        results = calculate_risk_metrics(portfolio)
        return {"risk_metrics": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/health")
async def health():
    return {"status": "ok"}