from fastapi import FastAPI
from app.api.endpoints import risk, stats

app = FastAPI()

# Register endpoints
app.include_router(risk.router, prefix="/risk", tags=["Risk"])
app.include_router(stats.router, prefix="/stats", tags=["Stats"])