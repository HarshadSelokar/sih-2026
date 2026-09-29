"""
Real-Time Train Tracking & Rescheduling Simulator Engine for SIH 26027
Simulates live GPS/OHE train movement, speed changes, signal aspects, delay propagation,
and real-time automatic rescheduling triggers for block planning integration.
"""

import sqlite3
import json
import time
import random
from datetime import datetime, timedelta

def simulate_live_step(db_path='railway_full_database.db', output_json='live_stream_snapshot.json'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT train_number, current_section_id, current_km_location, current_speed_kmph, delay_minutes, running_status FROM realtime_train_tracking;")
    active_trains = cursor.fetchall()

    updated_records = []

    for tr_num, sec_id, km_loc, speed, delay, status in active_trains:
        # Fetch train priority
        cursor.execute("SELECT train_name, train_type, max_permissible_speed_kmph, priority_rank FROM trains WHERE train_number = ?;", (tr_num,))
        tr_info = cursor.fetchone()
        tr_name, tr_type, max_spd, priority = tr_info

        # Simulate movement step (e.g. 30 seconds interval simulation)
        # Advance train by distance = speed (km/h) * (30/3600) hours
        distance_delta = (max(speed, 20) / 3600.0) * 30.0
        new_km = round(km_loc + distance_delta, 3)

        # Check for Temporary Speed Restriction (TSR) on track
        cursor.execute("SELECT restricted_speed_kmph, reason FROM temporary_speed_restrictions WHERE section_id = ? AND ? BETWEEN start_km AND end_km;", (sec_id, new_km))
        tsr_match = cursor.fetchone()

        if tsr_match:
            restricted_spd, reason = tsr_match
            new_speed = min(speed, restricted_spd)
            new_status = 'REGULATED_AT_STATION'
            signal_aspect = 'YELLOW'
            delay += 2 # Accumulate delay due to speed restriction
        else:
            new_speed = random.choice([max_spd, max_spd - 10, max_spd - 5]) if priority <= 3 else random.choice([60, 75, 80])
            new_status = 'RUNNING_ON_TIME' if delay <= 2 else 'RUNNING_LATE'
            signal_aspect = 'GREEN' if new_speed > 80 else 'DOUBLE_YELLOW'

        block_section = f"BLK_{sec_id}_{int(new_km)}"
        ts_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Update in database
        cursor.execute("""
            UPDATE realtime_train_tracking 
            SET current_km_location = ?, current_speed_kmph = ?, delay_minutes = ?, 
                running_status = ?, occupancy_block_section = ?, next_signal_aspect = ?, 
                last_gps_telemetry_timestamp = ?
            WHERE train_number = ?;
        """, (new_km, new_speed, delay, new_status, block_section, signal_aspect, ts_now, tr_num))

        updated_records.append({
            "train_number": tr_num,
            "train_name": tr_name,
            "train_type": tr_type,
            "section_id": sec_id,
            "current_km_location": new_km,
            "current_speed_kmph": new_speed,
            "delay_minutes": delay,
            "running_status": new_status,
            "occupancy_block_section": block_section,
            "next_signal_aspect": signal_aspect,
            "timestamp": ts_now
        })

    conn.commit()
    conn.close()

    # Save real-time live snapshot
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({
            "simulation_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "active_trains_count": len(updated_records),
            "live_trains": updated_records
        }, f, indent=2)

    print(f"[LIVE STREAM SIMULATOR] Updated {len(updated_records)} trains. Snapshot saved to '{output_json}'")

if __name__ == '__main__':
    simulate_live_step()
