# Tesla Companion 🚗

A personal monitoring dashboard for my Tesla Model 3 Long Range AWD (2019).

The goal of this project is to collect, store, and visualize vehicle data, providing insights into battery status, driving efficiency, charging history, and overall vehicle usage.

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Visualization:** Grafana
- **Infrastructure:** Docker Compose
- **Future integration:** Tesla Fleet API

## Project Structure

```text
tesla-companion/
├── backend/
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
├── database/
├── grafana/
├── .env
├── .gitignore
├── docker-compose.yml
└── README.md
```

## Architecture

The current setup consists of three main components:

- **FastAPI:** provides the backend API and will handle vehicle data collection.
- **PostgreSQL:** stores vehicle snapshots and historical data.
- **Grafana:** connects to PostgreSQL to visualize data through dashboards.

The services run in Docker containers and communicate through Docker Compose's internal network.

## Getting Started

### Prerequisites

- Python 3.12+
- Docker Desktop
- Git

### 1. Configure environment variables

Create a `.env` file in the project root:

```env
POSTGRES_DB=tesla_companion
POSTGRES_USER=tesla
POSTGRES_PASSWORD=your_local_password

GRAFANA_PORT=3000
POSTGRES_PORT=5433

DATABASE_URL=postgresql+psycopg://tesla:your_local_password@localhost:5433/tesla_companion
```

Use the same password in `POSTGRES_PASSWORD` and `DATABASE_URL`.

### 2. Start the infrastructure

From the project root:

```bash
docker compose up -d
```

This starts PostgreSQL and Grafana.

- Grafana: http://localhost:3000
- PostgreSQL: localhost:5433

### 3. Set up the Python environment

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r backend/requirements.txt
```

### 4. Start the API

Navigate to the backend directory:

```powershell
cd backend
python -m uvicorn main:app --reload
```

The API will be available at:

- Health check: http://localhost:8000/health
- Database health check: http://localhost:8000/health/database
- Interactive API documentation: http://localhost:8000/docs

## Database

The initial database schema includes a `vehicle_snapshots` table to store historical vehicle data.

| Column | Description |
|---|---|
| `id` | Unique snapshot identifier |
| `recorded_at` | Timestamp of the snapshot |
| `vehicle_id` | Vehicle identifier |
| `battery_level` | Battery charge level (%) |
| `estimated_range_km` | Estimated driving range (km) |
| `odometer_km` | Vehicle odometer (km) |
| `charging_state` | Current charging state |
| `plugged_in` | Whether the vehicle is plugged in |
| `outside_temp_c` | Outside temperature (°C) |
| `is_demo` | Indicates whether the record is demo data |
| `created_at` | Record creation timestamp |

An index on `recorded_at` supports time-based queries and historical analysis.

## Current Status

- [x] Project structure initialized
- [x] Docker Compose configuration
- [x] PostgreSQL container running
- [x] Grafana container running
- [x] Grafana connected to PostgreSQL
- [x] Initial database schema created
- [x] FastAPI application initialized
- [x] Database connection implemented
- [x] API and database health checks

## Roadmap

- [ ] Integrate Tesla Fleet API
- [ ] Implement vehicle data collection
- [ ] Store real vehicle snapshots
- [ ] Build Grafana dashboards
- [ ] Track charging sessions and energy consumption
- [ ] Analyze battery and driving efficiency
