# Indian Railways Multi-System Real-Time Data Suite for SIH 26027

> **Problem Statement**: **SIH26027** — *AI-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways*  
> **Integrated Datasets**: **COA** (Control Office Application), **TMS** (Track Management System), **TDMS** (Traction Distribution), **NTES** (Real-Time Tracking & Rescheduling).

---

## 1. Data Architecture & System Mapping

In Indian Railways, real-time train operations and maintenance planning depend on 4 core systems:

```
  +-------------------------------------------------------------------------+
  |                     INDIAN RAILWAYS DATA PLATFORM                       |
  +--------------------+--------------------+--------------------+----------+
                       |                    |                    |
                       v                    v                    v
            +--------------------+ +--------------------+ +--------------------+
            | COA (Control Office| | TMS (Track Maint.  | | TDMS (Electrical   |
            |    Application)    | |     System)        | |      OHE / PSI)    |
            | - Train Schedules  | | - Track Geometry   | | - Catenary wear    |
            | - Route Halts      | | - Tamping Windows  | | - Substation checks|
            | - Freight Forecast | | - Speed Restr (TSR)| | - Power Blocks     |
            +---------+----------+ +---------+----------+ +---------+----------+
                      |                      |                      |
                      +------------------+   |   +------------------+
                                         v   v   v
                             +-----------------------+
                             | Real-Time GPS / NTES  |
                             | Live Tracking Stream  |
                             | & Rescheduling Engine |
                             +-----------+-----------+
                                         |
                                         v
                             +-----------------------+
                             | SIH 26027 AI Automatic|
                             | Block Planning System |
                             +-----------------------+
```

---

## 2. The 4 Extracted Real-Time Datasets

### A. Train Schedule Data (`train_schedules.json` & `trains` table)
- **Source System**: **COA (Control Office Application) & FOIS (Freight Operations Information System)**
- **Contents**: Train numbers, names, train priority ranks (1 = Vande Bharat/Rajdhani down to 10 = Freight Coal), origin/destination, scheduled arrival/departure times, route halts, and maximum permissible speeds.
- **Key File**: [train_schedules.json](file:///E:/sih2026/train_schedules.json)

### B. Track Schedule & Corridor Data (`track_schedules.json`)
- **Source System**: **TMS (Track Management System)**
- **Contents**: Track corridor geometry index (TGI score), ballast cushions, sleeper density, planned BCM (Ballast Cleaning Machine) & CSM tamping machine windows, and Temporary Speed Restrictions (TSR orders e.g. 30 kmph restriction).
- **Key File**: [track_schedules.json](file:///E:/sih2026/track_schedules.json)

### C. Real-Time Live Tracking Telemetry (`realtime_tracking.json` & `live_stream_snapshot.json`)
- **Source System**: **NTES (National Train Enquiry System) & COA Live Section Feed**
- **Contents**: Real-time live train positions (KM chainage e.g., KM 812.450), live speeds (km/h), live delay minutes (+mins late), section block occupancy, and next signal aspect (`GREEN`, `DOUBLE_YELLOW`, `YELLOW`, `RED`).
- **Key Files**: [realtime_tracking.json](file:///E:/sih2026/realtime_tracking.json), [live_stream_snapshot.json](file:///E:/sih2026/live_stream_snapshot.json)

### D. Rescheduling & Disruption Data (`rescheduling_events.json`)
- **Source System**: **COA Rescheduling & Regulation Engine**
- **Contents**: Train retiming schedules, regulation at loop line stations, route diversions, and delay offsets caused by active multi-department maintenance blocks or signal disruptions.
- **Key File**: [rescheduling_events.json](file:///E:/sih2026/rescheduling_events.json)

---

## 3. Real-Time Telemetry & Tracking Simulator

You can simulate live real-time train movement, speed changes, signal aspects, and delay accumulation by running:

```bash
python realtime_tracking_simulator.py
```

This updates the SQLite database `railway_full_database.db` and writes a fresh JSON snapshot to [live_stream_snapshot.json](file:///E:/sih2026/live_stream_snapshot.json).

---

## 4. Summary of Generated Workspace Files

1. **[railway_full_schema.sql](file:///E:/sih2026/railway_full_schema.sql)**: Full SQL DDL schema for COA, TMS, NTES, and Rescheduling.
2. **[generate_railway_full_data.py](file:///E:/sih2026/generate_railway_full_data.py)**: Python dataset generator script.
3. **[railway_full_database.db](file:///E:/sih2026/railway_full_database.db)**: Unified SQLite database containing all 4 data modules.
4. **[train_schedules.json](file:///E:/sih2026/train_schedules.json)**: COA Train Timetables dataset.
5. **[track_schedules.json](file:///E:/sih2026/track_schedules.json)**: TMS Track maintenance & speed restrictions dataset.
6. **[realtime_tracking.json](file:///E:/sih2026/realtime_tracking.json)**: Real-time live train tracking stream dataset.
7. **[rescheduling_events.json](file:///E:/sih2026/rescheduling_events.json)**: Rescheduling & train regulation events dataset.
8. **[realtime_tracking_simulator.py](file:///E:/sih2026/realtime_tracking_simulator.py)**: Live tracking telemetry simulator engine.
