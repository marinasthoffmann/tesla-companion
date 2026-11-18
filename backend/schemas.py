from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class VehicleSnapshotCreate(BaseModel):
    vehicle_id: str | None = None
    
    battery_level: int | None = Field(
        default=None, 
        ge=0, 
        le=100
    )

    estimated_range_km: Decimal | None = Field(default=None, ge=0)
    odometer_km: Decimal | None = Field(default=None, ge=0)

    charging_state: str | None = None
    plugged_in: bool | None = None
    outside_temp_c: Decimal | None = None
    
    is_demo: bool = False

class VehicleSnapshotResponse(VehicleSnapshotCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    recorded_at: datetime
    created_at: datetime