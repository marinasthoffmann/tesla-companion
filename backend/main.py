import logging

from fastapi import FastAPI, HTTPException
from database import check_database_connection

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Tesla Companion API",
    description="Backend API for Tesla Companion",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "application": "Tesla Companion API",
    }

@app.get("/health/database")
def database_health_check():
    try:
        is_connected = check_database_connection()

        return {
            "status": "ok",
            "database": "connected"
        }
    except Exception as e:

        logger.exception("Database connection failed, error: %s", str(e))

        raise HTTPException(
            status_code=503,
            detail="Database connection failed"
        )