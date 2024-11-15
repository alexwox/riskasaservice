from fastapi import FastAPI
from app.routes import portfolio_routes

app = FastAPI(title="Financial Risk Analyzer API")

app.include_router(portfolio_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Financial Risk Analyzer API"}