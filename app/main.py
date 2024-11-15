from fastapi import FastAPI
from app.routes import portfolio_routes

app = FastAPI(
    title="Financial Risk Analyzer API",
    description="""
    This API provides financial risk analysis for investment portfolios.
    
    ## Features
    * Portfolio risk analysis
    * Value at Risk (VaR) calculation
    * Beta calculation against S&P 500
    * Portfolio diversification scoring
    
    ## Getting Started
    To analyze your portfolio, send a POST request to `/portfolio/analyze` with your portfolio holdings.
    """,
    version="1.0.0",
    contact={
        "name": "Alexander Woxstrom",
        "url": "https://woxst.ai",
        "email": "aw@woxst.ai",
    },
)

app.include_router(portfolio_routes.router)

@app.get("/", tags=["General"])
def root():
    """
    Root endpoint returning welcome message and basic API information.
    """
    return {"message": "Welcome to the Financial Risk Analyzer API"}