from pydantic import BaseModel, Field
from typing import Dict

class PortfolioRequest(BaseModel):
    holdings: Dict[str, float] = Field(
        ...,
        description="Dictionary of stock tickers and their quantities",
        example={"AAPL": 10, "GOOG": 5, "MSFT": 15}
    )

class RiskMetrics(BaseModel):
    value_at_risk_95: float = Field(..., description="95% Value at Risk")
    beta: float = Field(..., description="Portfolio Beta against S&P 500")
    diversification_score: float = Field(..., description="Portfolio diversification score (0-1)")

class PortfolioResponse(BaseModel):
    risk_metrics: RiskMetrics