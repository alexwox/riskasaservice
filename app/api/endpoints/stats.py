from fastapi import APIRouter
from app.schemas.portfolio import Portfolio
from app.services.portfolio import fit_t_distribution

router = APIRouter()

@router.post("/t_distribution")
async def fit_t_distribution_route(portfolio: Portfolio):
    return fit_t_distribution(portfolio)