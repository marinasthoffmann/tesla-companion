from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BigInteger, DateTime, func, String, Integer, Numeric, Boolean, ForeignKey

Base = declarative_base()

class VehicleSnapshot(Base):
    __tablename__ = "vehicle_snapshots"

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    recorded_at = Column(
        DateTime(timezone=True), 
        nullable=False, 
        server_default=func.now()
    )

    vehicle_id = Column(String(100), nullable=True)

    battery_level = Column(Integer, nullable=True)
    estimated_range_km = Column(Numeric(10, 2), nullable=True)
    odometer_km = Column(Numeric(10, 2), nullable=True)

    charging_state = Column(String(50), nullable=True)
    plugged_in = Column(Boolean, nullable=True)

    outside_temp_c = Column(Numeric(5, 2), nullable=True)

    is_demo = Column(Boolean, nullable=False, default=False)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )