from pydantic import BaseModel
from typing import List

class Portfolio(BaseModel):
    tickers: List[str]
    weights: List[float]