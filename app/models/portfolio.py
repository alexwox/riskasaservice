from typing import Dict

from pydantic import BaseModel, Field


class PortfolioRequest(BaseModel):
    holdings: Dict[str, int] = Field(...)

    model_config = {
        "json_schema_extra": {"examples": [{"holdings": {"AAPL": 10, "GOOG": 5}}]}
    }


class RiskMetrics(BaseModel):
    value_at_risk_95: float = Field(..., description="95% Value at Risk")
    beta: float = Field(..., description="Portfolio Beta against S&P 500")
    diversification_score: float = Field(
        ..., description="Portfolio diversification score (0-1)"
    )


class PortfolioResponse(BaseModel):
    risk_metrics: RiskMetrics
