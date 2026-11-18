from database import SessionLocal
from models import VehicleSnapshot

def main():
    with SessionLocal() as session:
        snapshots = (
            session.query(VehicleSnapshot)
            .order_by(VehicleSnapshot.recorded_at.desc())
            .limit(10)
            .all()
        )

        print(f"Found {len(snapshots)} snapshots")

        for snapshot in snapshots:
            print(
                f"ID: {snapshot.id} | "
                f"Battery: {snapshot.battery_level}% | "
                f"Range: {snapshot.estimated_range_km} km | "
                f"Odometer: {snapshot.odometer_km} km | "
                f"Demo: {snapshot.is_demo}"
            )


if __name__ == "__main__":
    main()
