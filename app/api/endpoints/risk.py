from fastapi import APIRouter
from app.schemas.portfolio import Portfolio
from app.services.portfolio import (
    calculate_sharpe_ratio, calculate_var, calculate_cvar
)

router = APIRouter()

@router.post("/sharpe_ratio")
async def get_sharpe_ratio(portfolio: Portfolio):
    return {"sharpe_ratio": calculate_sharpe_ratio(portfolio)}

@router.post("/var")
async def get_var(portfolio: Portfolio):
    return {"var": calculate_var(portfolio)}

@router.post("/cvar")
async def get_cvar(portfolio: Portfolio):
    return {"cvar": calculate_cvar(portfolio)}