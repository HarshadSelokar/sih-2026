"""
Comprehensive Indian Railways Data Generator for SIH 26027
Generates COA Train Schedules, TMS Track Maintenance Schedules, 
Real-Time Live Train Telemetry Stream, and Rescheduling Disruption Records.
"""

import sqlite3
import json
import random
from datetime import datetime, timedelta

def create_tables(conn):
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trains (
        train_number TEXT PRIMARY KEY,
        train_name TEXT NOT NULL,
        train_type TEXT,
        priority_rank INTEGER NOT NULL,
        origin_station TEXT NOT NULL,
        destination_station TEXT NOT NULL,
        max_permissible_speed_kmph INTEGER DEFAULT 130,
        rake_length INTEGER DEFAULT 22,
        loco_type TEXT DEFAULT 'WAP-7'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS train_schedule_routes (
        schedule_id TEXT PRIMARY KEY,
        train_number TEXT REFERENCES trains(train_number),
        section_id TEXT NOT NULL,
        sequence_no INTEGER NOT NULL,
        station_code TEXT,
        scheduled_arrival TEXT,
        scheduled_departure TEXT,
        dwell_minutes INTEGER DEFAULT 0,
        entry_km REAL NOT NULL,
        exit_km REAL NOT NULL,
        scheduled_speed_kmph INTEGER DEFAULT 110
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS track_corridor_assets (
        track_id TEXT PRIMARY KEY,
        section_id TEXT NOT NULL,
        track_line TEXT,
        start_km REAL NOT NULL,
        end_km REAL NOT NULL,
        rail_weight_kg TEXT,
        sleeper_density INTEGER,
        ballast_cushion_mm INTEGER,
        tgi_score REAL,
        last_tamping_date TEXT,
        last_deep_screening_date TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tms_track_schedules (
        track_schedule_id TEXT PRIMARY KEY,
        section_id TEXT NOT NULL,
        start_km REAL NOT NULL,
        end_km REAL NOT NULL,
        maintenance_activity TEXT NOT NULL,
        track_block_duration_minutes INTEGER NOT NULL,
        required_machinery TEXT,
        urgency_level TEXT,
        planned_date TEXT NOT NULL,
        status TEXT DEFAULT 'PLANNED'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS temporary_speed_restrictions (
        tsr_id TEXT PRIMARY KEY,
        section_id TEXT NOT NULL,
        start_km REAL NOT NULL,
        end_km REAL NOT NULL,
        restricted_speed_kmph INTEGER NOT NULL,
        normal_speed_kmph INTEGER DEFAULT 130,
        reason TEXT NOT NULL,
        issued_date TEXT NOT NULL,
        expected_removal_date TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS realtime_train_tracking (
        tracking_id TEXT PRIMARY KEY,
        train_number TEXT REFERENCES trains(train_number),
        current_section_id TEXT NOT NULL,
        current_km_location REAL NOT NULL,
        current_speed_kmph INTEGER NOT NULL,
        delay_minutes INTEGER DEFAULT 0,
        running_status TEXT,
        occupancy_block_section TEXT,
        next_signal_aspect TEXT,
        last_gps_telemetry_timestamp TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS train_rescheduling_events (
        reschedule_id TEXT PRIMARY KEY,
        train_number TEXT REFERENCES trains(train_number),
        original_departure_time TEXT NOT NULL,
        rescheduled_departure_time TEXT NOT NULL,
        delay_offset_minutes INTEGER NOT NULL,
        cause_category TEXT,
        reschedule_reason TEXT NOT NULL,
        regulation_station TEXT,
        action_type TEXT,
        created_at TEXT
    );
    """)

    conn.commit()

def generate_all_data(db_path='railway_full_database.db'):
    conn = sqlite3.connect(db_path)
    create_tables(conn)
    cursor = conn.cursor()

    # Clear tables
    for t in ['train_rescheduling_events', 'realtime_train_tracking', 'temporary_speed_restrictions', 
              'tms_track_schedules', 'track_corridor_assets', 'train_schedule_routes', 'trains']:
        cursor.execute(f"DELETE FROM {t};")

    now = datetime.now()

    # 1. Trains Master (COA Data)
    trains_list = [
        ('20912', 'Nagpur - Bilaspur Vande Bharat Express', 'VANDE_BHARAT', 1, 'Nagpur (NGP)', 'Bilaspur (BSP)', 130, 16, 'VB-TRAINSET'),
        ('12105', 'Vidarbha Superfast Express', 'SUPERFAST', 3, 'Mumbai CSMT', 'Gondia (G)', 110, 24, 'WAP-7'),
        ('12833', 'Howrah - Ahmedabad SF Express', 'SUPERFAST', 3, 'Howrah (HWH)', 'Ahmedabad (ADI)', 110, 22, 'WAP-7'),
        ('12656', 'Navjeevan Express', 'SUPERFAST', 4, 'Chennai Central', 'Ahmedabad (ADI)', 110, 24, 'WAP-7'),
        ('18030', 'Shalitmar - Mumbai LTT Express', 'EXPRESS', 5, 'Shalitmar (SHM)', 'Mumbai LTT', 100, 22, 'WAP-4'),
        ('01124', 'Nagpur - Wardha MEMU Passenger', 'PASSENGER', 7, 'Nagpur (NGP)', 'Wardha (WR)', 90, 12, 'MEMU'),
        ('GOODS_CONT_901', 'JNPT Container Freight (BTPN)', 'FREIGHT_CONTAINER', 8, 'JNPT Mumbai', 'Dadri ICD', 75, 45, 'WAG-9H'),
        ('GOODS_COAL_405', 'WCL Coal Rake Freight (BOXN)', 'FREIGHT_COAL', 9, 'Umrer Colliery', 'NTPC Mauda Power Station', 60, 59, 'WAG-9')
    ]
    cursor.executemany("INSERT INTO trains VALUES (?,?,?,?,?,?,?,?,?);", trains_list)

    # 2. Train Schedule Routes (COA Schedules)
    schedules_list = []
    sections = ['SEC_NGP_WR_UP', 'SEC_NGP_WR_DN', 'SEC_WR_BD_UP', 'SEC_WR_BD_DN']
    
    for tr in trains_list:
        tr_num = tr[0]
        base_time = now.replace(hour=6, minute=0, second=0) + timedelta(minutes=random.randint(0, 720))
        
        sec_id = 'SEC_NGP_WR_UP' if random.choice([True, False]) else 'SEC_NGP_WR_DN'
        start_k = 785.0
        
        for idx in range(1, 4):
            sch_id = f"SCH_{tr_num}_SEC_{idx}"
            arr_time = base_time + timedelta(minutes=(idx-1)*35)
            dep_time = arr_time + timedelta(minutes=2 if tr[2] in ['SUPERFAST', 'VANDE_BHARAT'] else 10)
            
            end_k = start_k + 26.3
            station = 'Ajni (AJNI)' if idx == 1 else ('Sindi (SNI)' if idx == 2 else 'Wardha (WR)')
            
            row = (sch_id, tr_num, sec_id, idx, station, 
                   arr_time.strftime('%Y-%m-%d %H:%M:%S'), 
                   dep_time.strftime('%Y-%m-%d %H:%M:%S'), 
                   2 if idx < 3 else 5, round(start_k, 3), round(end_k, 3), tr[6])
            schedules_list.append(row)
            start_k = end_k
            base_time = dep_time

    cursor.executemany("INSERT INTO train_schedule_routes VALUES (?,?,?,?,?,?,?,?,?,?,?);", schedules_list)

    # 3. Track Corridor Assets & TMS Maintenance Schedules
    track_assets = [
        ('TRK_NGP_WR_UP_01', 'SEC_NGP_WR_UP', 'UP', 785.0, 810.0, '60kg 90UTS', 1660, 350, 82.5, '2025-11-10', '2024-06-15'),
        ('TRK_NGP_WR_UP_02', 'SEC_NGP_WR_UP', 'UP', 810.0, 835.0, '60kg 90UTS', 1660, 300, 68.0, '2025-08-20', '2023-12-10'), # Low TGI score!
        ('TRK_NGP_WR_DN_01', 'SEC_NGP_WR_DN', 'DOWN', 785.0, 820.0, '60kg 90UTS', 1660, 350, 88.0, '2025-12-01', '2024-08-01')
    ]
    cursor.executemany("INSERT INTO track_corridor_assets VALUES (?,?,?,?,?,?,?,?,?,?,?);", track_assets)

    tms_schedules = [
        ('TMS_SCH_2026_01', 'SEC_NGP_WR_UP', 812.0, 818.5, 'BCM Ballast Cleaning & Deep Screening', 240, 'BCM Machine 802 + DGS', 'CRITICAL', (now + timedelta(days=2)).strftime('%Y-%m-%d'), 'PLANNED'),
        ('TMS_SCH_2026_02', 'SEC_NGP_WR_UP', 825.0, 830.0, 'Track Tamping with CSM Machine', 180, 'CSM Tamper 09-32', 'HIGH', (now + timedelta(days=1)).strftime('%Y-%m-%d'), 'REQUESTED'),
        ('TMS_SCH_2026_03', 'SEC_NGP_WR_DN', 795.0, 802.0, 'Through Rail Renewal (TRR)', 300, 'TRT Rail Threader Machine', 'MEDIUM', (now + timedelta(days=4)).strftime('%Y-%m-%d'), 'PLANNED')
    ]
    cursor.executemany("INSERT INTO tms_track_schedules VALUES (?,?,?,?,?,?,?,?,?,?);", tms_schedules)

    # Temporary Speed Restrictions (TSR)
    tsr_list = [
        ('TSR_2026_101', 'SEC_NGP_WR_UP', 812.0, 814.5, 30, 130, 'Deep screening track work in progress', (now - timedelta(days=3)).strftime('%Y-%m-%d'), (now + timedelta(days=5)).strftime('%Y-%m-%d')),
        ('TSR_2026_102', 'SEC_NGP_WR_DN', 838.0, 840.0, 45, 110, 'Bridge approach track consolidation', (now - timedelta(days=1)).strftime('%Y-%m-%d'), (now + timedelta(days=10)).strftime('%Y-%m-%d'))
    ]
    cursor.executemany("INSERT INTO temporary_speed_restrictions VALUES (?,?,?,?,?,?,?,?,?);", tsr_list)

    # 4. Real-Time Train Tracking Data (Live NTES/COA Simulation Stream)
    tracking_list = []
    statuses = ['RUNNING_ON_TIME', 'RUNNING_LATE', 'DETAINED_AT_SIGNAL', 'REGULATED_AT_STATION']
    aspects = ['GREEN', 'DOUBLE_YELLOW', 'YELLOW', 'RED']

    for tr in trains_list:
        tr_num = tr[0]
        trk_id = f"TRK_LIVE_{tr_num}"
        sec_id = random.choice(['SEC_NGP_WR_UP', 'SEC_NGP_WR_DN'])
        km_loc = round(random.uniform(786.0, 860.0), 3)
        
        delay = 0 if tr[2] == 'VANDE_BHARAT' else (random.randint(5, 45) if tr[2] == 'FREIGHT_COAL' else random.randint(0, 20))
        status = 'RUNNING_ON_TIME' if delay == 0 else random.choice(statuses)
        speed = 0 if status == 'DETAINED_AT_SIGNAL' else random.randint(45, tr[6])
        aspect = 'RED' if speed == 0 else ('GREEN' if speed > 90 else random.choice(aspects))
        
        block_sec = f"BLK_{sec_id}_{int(km_loc)}"
        ts_str = now.strftime('%Y-%m-%d %H:%M:%S')

        row = (trk_id, tr_num, sec_id, km_loc, speed, delay, status, block_sec, aspect, ts_str)
        tracking_list.append(row)

    cursor.executemany("INSERT INTO realtime_train_tracking VALUES (?,?,?,?,?,?,?,?,?,?);", tracking_list)

    # 5. Rescheduling & Disruption Events
    rescheduling_list = []
    causes = [
        ('POWER_BLOCK_MAINTENANCE', 'OHE Power block applied for contact wire replacement between Sindi & Wardha', 'Sindi (SNI)', 'REGULATED'),
        ('TRACK_MAINTENANCE', 'TMS Deep screening block extended by 45 mins at KM 814', 'Ajni (AJNI)', 'RETIMED'),
        ('SIGNAL_FAILURE', 'Axle counter failure at Wardha North Cabin', 'Wardha (WR)', 'REGULATED'),
        ('POWER_BLOCK_MAINTENANCE', 'Integrated Multi-Dept Power & Track block on UP Line', 'Nagpur (NGP)', 'DIVERTED')
    ]

    for i, (cause_cat, desc, reg_st, act_type) in enumerate(causes, 1):
        r_id = f"RESCHED_2026_{i:03d}"
        tr_num = trains_list[i % len(trains_list)][0]
        orig_dep = now + timedelta(hours=i)
        offset = random.randint(25, 90)
        new_dep = orig_dep + timedelta(minutes=offset)

        row = (r_id, tr_num, orig_dep.strftime('%Y-%m-%d %H:%M:%S'), 
               new_dep.strftime('%Y-%m-%d %H:%M:%S'), offset, cause_cat, desc, reg_st, act_type, now.strftime('%Y-%m-%d %H:%M:%S'))
        rescheduling_list.append(row)

    cursor.executemany("INSERT INTO train_rescheduling_events VALUES (?,?,?,?,?,?,?,?,?,?);", rescheduling_list)

    conn.commit()

    # Export individual JSON files for each requested data type
    datasets_to_export = {
        'train_schedules.json': ['trains', 'train_schedule_routes'],
        'track_schedules.json': ['track_corridor_assets', 'tms_track_schedules', 'temporary_speed_restrictions'],
        'realtime_tracking.json': ['realtime_train_tracking'],
        'rescheduling_events.json': ['train_rescheduling_events']
    }

    for json_file, tables in datasets_to_export.items():
        out_dict = {}
        for tbl in tables:
            cursor.execute(f"SELECT * FROM {tbl};")
            cols = [c[0] for c in cursor.description]
            out_dict[tbl] = [dict(zip(cols, r)) for r in cursor.fetchall()]
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(out_dict, f, indent=2)
        print(f"[SUCCESS] Exported '{json_file}'")

    print(f"[SUCCESS] SQLite database successfully generated: '{db_path}'")
    conn.close()

if __name__ == '__main__':
    generate_all_data()
