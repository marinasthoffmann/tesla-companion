
from decimal import Decimal

from database import SessionLocal
from models import VehicleSnapshot


def main():
    snapshot = VehicleSnapshot(
        vehicle_id="tesla_model_3_2019",
        battery_level=74,
        estimated_range_km=Decimal("365.00"),
        odometer_km=Decimal("85492.00"),
        charging_state="Disconnected",
        plugged_in=False,
        outside_temp_c=Decimal("8.50"),
        is_demo=True,
    )

    with SessionLocal() as session:
        session.add(snapshot)
        session.commit()
        session.refresh(snapshot)

        print("Snapshot saved successfully!")
        print(f"ID: {snapshot.id}")
        print(f"Recorded at: {snapshot.recorded_at}")
        print(f"Battery: {snapshot.battery_level}%")
        print(f"Range: {snapshot.estimated_range_km} km")
        print(f"Odometer: {snapshot.odometer_km} km")


if __name__ == "__main__":
    main()
