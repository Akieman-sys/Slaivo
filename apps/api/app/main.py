from fastapi import FastAPI
from app.api.routes.webhooks import router as webhook_router

app = FastAPI(title="SLAIVO CARGO API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(webhook_router, prefix="/webhooks", tags=["webhooks"])