import logging
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from schemas import VehicleSnapshotCreate, VehicleSnapshotResponse
from database import check_database_connection, get_db
from sqlalchemy.orm import Session
from models import VehicleSnapshot

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

@app.post(
    "/vehicle/snapshot",
    response_model=VehicleSnapshotResponse,
    status_code=status.HTTP_201_CREATED
)
def create_vehicle_snapshot(
    snapshot_data: VehicleSnapshotCreate,
    db: Session = Depends(get_db)
):
    snapshot = VehicleSnapshot(**snapshot_data.model_dump())

    try:
        db.add(snapshot)
        db.commit()
        db.refresh(snapshot)

        return snapshot
    except Exception as e:
        logger.exception("Failed to create vehicle snapshot, error: %s", str(e))
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to create vehicle snapshot"
        )

@app.get(
    "/vehicle/snapshots",
    response_model=list[VehicleSnapshotResponse]
)
def get_vehicle_snapshots(
    limit: int = 100,
    is_demo: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    if limit <= 0 or limit > 1000:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 1000"
        )

    query = db.query(VehicleSnapshot)

    if is_demo is not None:
        query = query.filter(
            VehicleSnapshot.is_demo == is_demo
            )

    snapshots = (
        query
        .order_by(VehicleSnapshot.recorded_at.desc())
        .limit(limit)
        .all()
    )
    
    return snapshots