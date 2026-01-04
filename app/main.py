"""
Delay Notifier API

遅延通知システムのメインアプリケーション
"""

from fastapi import FastAPI
from app.routers import user, auth, lines, settings, events, delays
from app.database import engine, Base

from app.models import user as user_model

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Delay Notifier API",
    description="電車遅延通知システムのAPI",
    version="1.0.0"
)

app.include_router(user.router, prefix="/v1/users", tags=["users"])

app.include_router(auth.router, prefix="/v1/auth", tags=["auth"])

app.include_router(lines.router, prefix="/v1/lines", tags=["lines"])

app.include_router(settings.router, prefix="/v1/settings", tags=["settings"])

app.include_router(events.router, prefix="/v1/events", tags=["events"])

app.include_router(events.router, prefix="/v1/certificates", tags=["certificates"])

app.include_router(events.router, prefix="/v1/verify", tags=["verify"])

app.include_router(delays.router, prefix="/v1/delays", tags=["delays"])

@app.get("/health", tags=["health"])
def health():
    return {"ok": True}