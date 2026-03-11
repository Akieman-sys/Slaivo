from fastapi import FastAPI
from app.api.routes.webhooks import router as webhook_router
from app.api.routes.inbox import router as inbox_router
from app.api.routes.notifications import router as notifications_router

app = FastAPI(title="SLAIVO CARGO API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(webhook_router, prefix="/webhooks", tags=["webhooks"])
app.include_router(inbox_router, prefix="/inbox", tags=["inbox"])
app.include_router(notifications_router, prefix="/notifications", tags=["notifications"])