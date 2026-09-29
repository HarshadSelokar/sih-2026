"""
TDMS (Traction Distribution Management System) Synthetic Data Generator
Designed for SIH 2026 Problem Statement: SIH26027
(AI-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways)
"""

import sqlite3
import json
import random
from datetime import datetime, timedelta

def create_sqlite_tables(conn):
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trd_zones (
        zone_id TEXT PRIMARY KEY,
        zone_name TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trd_divisions (
        division_id TEXT PRIMARY KEY,
        zone_id TEXT REFERENCES trd_zones(zone_id),
        division_name TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trd_sections (
        section_id TEXT PRIMARY KEY,
        division_id TEXT REFERENCES trd_divisions(division_id),
        section_name TEXT NOT NULL,
        start_km REAL NOT NULL,
        end_km REAL NOT NULL,
        line_type TEXT CHECK (line_type IN ('UP', 'DOWN', 'THIRD', 'FOURTH', 'YARD', 'BYPASS')),
        electrified_voltage_kv REAL DEFAULT 25.0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS psi_installations (
        installation_id TEXT PRIMARY KEY,
        section_id TEXT REFERENCES trd_sections(section_id),
        installation_type TEXT CHECK (installation_type IN ('TSS', 'SP', 'SSP', 'FP')),
        location_km REAL NOT NULL,
        grid_supply_voltage_kv REAL DEFAULT 132.0,
        num_transformers INTEGER DEFAULT 2,
        scada_enabled BOOLEAN DEFAULT 1,
        operational_status TEXT DEFAULT 'ACTIVE'
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ohe_masts (
        mast_id TEXT PRIMARY KEY,
        section_id TEXT REFERENCES trd_sections(section_id),
        location_km REAL NOT NULL,
        mast_number TEXT NOT NULL,
        track_line TEXT NOT NULL,
        structure_type TEXT,
        catenary_wire_type TEXT DEFAULT '65 sq.mm Cadmium Copper',
        contact_wire_type TEXT DEFAULT '107 sq.mm Hard Drawn Copper',
        stagger_mm INTEGER,
        height_meters REAL DEFAULT 5.50,
        installation_date TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trd_depots (
        depot_id TEXT PRIMARY KEY,
        division_id TEXT REFERENCES trd_divisions(division_id),
        depot_name TEXT NOT NULL,
        location_station TEXT NOT NULL,
        contact_number TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tower_wagons (
        tw_id TEXT PRIMARY KEY,
        depot_id TEXT REFERENCES trd_depots(depot_id),
        tw_code TEXT UNIQUE NOT NULL,
        tw_type TEXT CHECK (tw_type IN ('4-WHEELER', '8-WHEELER', 'NETRA_SPECIAL')),
        max_speed_kmph INTEGER DEFAULT 110,
        operational_status TEXT DEFAULT 'AVAILABLE',
        last_fitness_cert_date TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tdms_defects (
        defect_id TEXT PRIMARY KEY,
        section_id TEXT REFERENCES trd_sections(section_id),
        mast_id TEXT REFERENCES ohe_masts(mast_id),
        installation_id TEXT REFERENCES psi_installations(installation_id),
        subsystem TEXT CHECK (subsystem IN ('OHE', 'PSI', 'SCADA', 'BONDING', 'TOWER_WAGON')),
        defect_category TEXT NOT NULL,
        severity TEXT CHECK (severity IN ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW')),
        detected_by TEXT,
        detection_date TEXT NOT NULL,
        target_rectification_date TEXT,
        status TEXT DEFAULT 'OPEN' CHECK (status IN ('OPEN', 'BLOCK_REQUESTED', 'BLOCK_APPROVED', 'RESOLVED', 'DEFERRED')),
        power_block_required BOOLEAN DEFAULT 1,
        traffic_block_required BOOLEAN DEFAULT 0,
        estimated_work_duration_minutes INTEGER NOT NULL,
        required_manpower INTEGER DEFAULT 4,
        tower_wagon_required BOOLEAN DEFAULT 1,
        description TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tdms_maintenance_schedules (
        schedule_id TEXT PRIMARY KEY,
        section_id TEXT REFERENCES trd_sections(section_id),
        asset_type TEXT CHECK (asset_type IN ('OHE_SPAN', 'TSS_TRANSFORMER', 'CIRCUIT_BREAKER', 'ISOLATOR', 'AT_TRANSFORMER', 'NEUTRAL_SECTION')),
        asset_id TEXT NOT NULL,
        maintenance_type TEXT CHECK (maintenance_type IN ('MONTHLY', 'QUARTERLY', 'HALF_YEARLY', 'ANNUAL', 'IOH', 'POH')),
        last_done_date TEXT NOT NULL,
        due_date TEXT NOT NULL,
        overdue_days INTEGER DEFAULT 0,
        urgency_score REAL DEFAULT 0.0,
        estimated_duration_minutes INTEGER NOT NULL,
        power_block_required BOOLEAN DEFAULT 1,
        traffic_block_required BOOLEAN DEFAULT 0,
        status TEXT DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'SCHEDULED', 'COMPLETED', 'OVERDUE'))
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tdms_block_requests (
        block_request_id TEXT PRIMARY KEY,
        section_id TEXT REFERENCES trd_sections(section_id),
        start_km REAL NOT NULL,
        end_km REAL NOT NULL,
        track_line TEXT CHECK (track_line IN ('UP', 'DOWN', 'BOTH', 'YARD')),
        isolation_post_from TEXT REFERENCES psi_installations(installation_id),
        isolation_post_to TEXT REFERENCES psi_installations(installation_id),
        block_type TEXT CHECK (block_type IN ('POWER_BLOCK', 'TRAFFIC_AND_POWER_BLOCK', 'SHADOW_BLOCK', 'EMERGENCY_POWER_BLOCK')),
        requested_duration_minutes INTEGER NOT NULL,
        preferred_window_start TEXT,
        preferred_window_end TEXT,
        associated_defect_ids TEXT,
        associated_schedule_ids TEXT,
        depot_id TEXT REFERENCES trd_depots(depot_id),
        assigned_tw_id TEXT REFERENCES tower_wagons(tw_id),
        priority_level INTEGER CHECK (priority_level BETWEEN 1 AND 5),
        status TEXT DEFAULT 'SUBMITTED_TO_BDMS',
        created_at TEXT
    );
    """)

    conn.commit()

def generate_data(db_path='tdms_database.db', json_out_path='tdms_data.json'):
    conn = sqlite3.connect(db_path)
    create_sqlite_tables(conn)
    cursor = conn.cursor()

    # Clear existing data
    tables = ['tdms_block_requests', 'tdms_maintenance_schedules', 'tdms_defects', 'tower_wagons', 
              'trd_depots', 'ohe_masts', 'psi_installations', 'trd_sections', 'trd_divisions', 'trd_zones']
    for t in tables:
        cursor.execute(f"DELETE FROM {t};")

    # 1. Zone & Division
    cursor.execute("INSERT INTO trd_zones VALUES ('CR', 'Central Railway');")
    cursor.execute("INSERT INTO trd_divisions VALUES ('NGP', 'CR', 'Nagpur Division');")

    # 2. Sections
    sections_data = [
        ('SEC_NGP_WR_UP', 'NGP', 'Nagpur - Wardha UP Line', 785.0, 864.0, 'UP', 25.0),
        ('SEC_NGP_WR_DN', 'NGP', 'Nagpur - Wardha DOWN Line', 785.0, 864.0, 'DOWN', 25.0),
        ('SEC_WR_BD_UP', 'NGP', 'Wardha - Badnera UP Line', 864.0, 959.0, 'UP', 25.0),
        ('SEC_WR_BD_DN', 'NGP', 'Wardha - Badnera DOWN Line', 864.0, 959.0, 'DOWN', 25.0)
    ]
    cursor.executemany("INSERT INTO trd_sections VALUES (?,?,?,?,?,?,?);", sections_data)

    # 3. PSI Installations (Substations & Sectioning Posts)
    psi_data = [
        ('PSI_TSS_AJNI', 'SEC_NGP_WR_UP', 'TSS', 788.500, 132.0, 2, 1, 'ACTIVE'),
        ('PSI_SSP_SINDI', 'SEC_NGP_WR_UP', 'SSP', 812.200, 132.0, 0, 1, 'ACTIVE'),
        ('PSI_SP_BUTIBORI', 'SEC_NGP_WR_UP', 'SP', 830.400, 132.0, 0, 1, 'ACTIVE'),
        ('PSI_TSS_WR', 'SEC_NGP_WR_UP', 'TSS', 863.800, 132.0, 2, 1, 'ACTIVE'),
        ('PSI_SSP_SEVAGRAM', 'SEC_WR_BD_UP', 'SSP', 868.100, 132.0, 0, 1, 'ACTIVE'),
        ('PSI_TSS_DMN', 'SEC_WR_BD_UP', 'TSS', 910.500, 132.0, 2, 1, 'ACTIVE')
    ]
    cursor.executemany("INSERT INTO psi_installations VALUES (?,?,?,?,?,?,?,?);", psi_data)

    # 4. TRD Depots & Tower Wagons
    depots_data = [
        ('DEP_AJNI', 'NGP', 'Ajni TRD Depot', 'Ajni', '+91-712-2900101'),
        ('DEP_WR', 'NGP', 'Wardha TRD Depot', 'Wardha', '+91-7152-240102'),
        ('DEP_BD', 'NGP', 'Badnera TRD Depot', 'Badnera', '+91-721-2580103')
    ]
    cursor.executemany("INSERT INTO trd_depots VALUES (?,?,?,?,?);", depots_data)

    tw_data = [
        ('TW_8W_01', 'DEP_AJNI', '8W-NETRA-AJNI-01', 'NETRA_SPECIAL', 110, 'AVAILABLE', '2026-01-15'),
        ('TW_8W_02', 'DEP_WR', '8W-TRD-WR-02', '8-WHEELER', 110, 'AVAILABLE', '2026-02-10'),
        ('TW_4W_03', 'DEP_BD', '4W-TRD-BD-03', '4-WHEELER', 75, 'AVAILABLE', '2026-03-01')
    ]
    cursor.executemany("INSERT INTO tower_wagons VALUES (?,?,?,?,?,?,?);", tw_data)

    # 5. OHE Masts Generation
    mast_ids = []
    masts_list = []
    for sec_id, _, _, start_k, end_k, line, _ in sections_data:
        curr_k = start_k
        idx = 1
        while curr_k <= min(start_k + 15.0, end_k): # Generate sample masts for 15km stretch
            mast_no = f"{int(curr_k)}/{idx*2}"
            m_id = f"MAST_{sec_id}_{mast_no.replace('/', '_')}"
            mast_ids.append((m_id, sec_id, curr_k, mast_no, line))
            masts_list.append((m_id, sec_id, round(curr_k, 3), mast_no, line, 'Single Mast', 
                               '65 sq.mm Cadmium Copper', '107 sq.mm Hard Drawn Copper', 
                               random.choice([-200, -100, 0, 100, 200]), 5.55, '2018-05-20'))
            curr_k += 0.075 # ~75 meters span
            idx += 1

    cursor.executemany("INSERT INTO ohe_masts VALUES (?,?,?,?,?,?,?,?,?,?,?);", masts_list)

    # 6. TDMS Defects Generation
    defect_categories = [
        ('Contact Wire Wear > 20%', 'CRITICAL', 'Thermovision NETRA', 180, True, True),
        ('Insulator Flashover & Cracks', 'CRITICAL', 'Foot Patrol', 120, True, False),
        ('Cantilever Imbalance & Tilt', 'HIGH', 'Cab Inspection', 150, True, True),
        ('Dropper Loose / Missing', 'HIGH', 'Foot Patrol', 90, True, True),
        ('Hotspot on Isolator Jumper Contact', 'HIGH', 'Thermovision NETRA', 120, True, False),
        ('Bird Nest Near Live 25kV Line', 'MEDIUM', 'Foot Patrol', 60, True, False),
        ('Tree Vegetation Encroachment in Clearance Zone', 'MEDIUM', 'Foot Patrol', 120, True, False),
        ('Earth Bonding Defective / Stolen', 'LOW', 'Foot Patrol', 90, False, False)
    ]

    now = datetime.now()
    defects_inserted = []
    
    for i in range(1, 26):
        d_id = f"DEF_TRD_2026_{i:03d}"
        m_id, sec_id, km, mast_no, line = random.choice(mast_ids)
        cat, sev, det_by, dur, tw_req, tf_req = random.choice(defect_categories)
        
        det_date = (now - timedelta(days=random.randint(1, 20))).strftime('%Y-%m-%d %H:%M:%S')
        tgt_date = (now + timedelta(days=random.randint(1, 7))).strftime('%Y-%m-%d %H:%M:%S')
        
        status = random.choice(['OPEN', 'BLOCK_REQUESTED', 'BLOCK_REQUESTED', 'OPEN'])
        desc = f"Observed {cat} at mast {mast_no} on line {line} at KM {km:.3f}."
        
        row = (d_id, sec_id, m_id, 'PSI_SSP_SINDI' if i % 5 == 0 else None, 'OHE', cat, sev, det_by, 
               det_date, tgt_date, status, 1, 1 if tf_req else 0, dur, random.randint(4, 8), 1 if tw_req else 0, desc)
        defects_inserted.append(row)

    cursor.executemany("INSERT INTO tdms_defects VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", defects_inserted)

    # 7. Maintenance Schedules (Routine Overdue & Upcoming)
    schedules_inserted = []
    maint_types = [('OHE_SPAN', 'ANNUAL', 180, 365), ('TSS_TRANSFORMER', 'HALF_YEARLY', 240, 180), 
                   ('CIRCUIT_BREAKER', 'QUARTERLY', 120, 90), ('NEUTRAL_SECTION', 'MONTHLY', 90, 30)]

    for i in range(1, 16):
        sch_id = f"SCH_TRD_2026_{i:03d}"
        m_id, sec_id, km, mast_no, line = random.choice(mast_ids)
        asset_type, m_type, dur, cycle_days = random.choice(maint_types)
        
        days_offset = random.randint(-40, 15) # negative = overdue
        due_dt = now.date() + timedelta(days=days_offset)
        last_dt = due_dt - timedelta(days=cycle_days)
        
        overdue_days = max(0, (now.date() - due_dt).days)
        urgency = round(min(10.0, (overdue_days / 10.0) + (3.0 if m_type == 'ANNUAL' else 1.5)), 2)
        status = 'OVERDUE' if overdue_days > 0 else 'PENDING'

        row = (sch_id, sec_id, asset_type, m_id, m_type, last_dt.strftime('%Y-%m-%d'), 
               due_dt.strftime('%Y-%m-%d'), overdue_days, urgency, dur, 1, 0, status)
        schedules_inserted.append(row)

    cursor.executemany("INSERT INTO tdms_maintenance_schedules VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);", schedules_inserted)

    # 8. TDMS Block Requests (Payload generated for AI Block Planning integration)
    block_requests_inserted = []
    for i in range(1, 11):
        req_id = f"PBR_TRD_2026_{i:03d}"
        sec_id = random.choice(['SEC_NGP_WR_UP', 'SEC_NGP_WR_DN', 'SEC_WR_BD_UP'])
        start_km = round(random.uniform(790.0, 840.0), 3)
        end_km = round(start_km + random.uniform(2.0, 8.0), 3)
        
        win_start = (now + timedelta(days=random.randint(1, 3), hours=random.randint(6, 14))).strftime('%Y-%m-%d %H:%M:%S')
        win_end = (datetime.strptime(win_start, '%Y-%m-%d %H:%M:%S') + timedelta(hours=4)).strftime('%Y-%m-%d %H:%M:%S')
        
        def_ids = [defects_inserted[random.randint(0, len(defects_inserted)-1)][0] for _ in range(random.randint(1, 3))]
        sch_ids = [schedules_inserted[random.randint(0, len(schedules_inserted)-1)][0] for _ in range(random.randint(0, 2))]
        
        priority = random.choice([1, 2, 2, 3, 4])
        b_type = 'EMERGENCY_POWER_BLOCK' if priority == 1 else 'POWER_BLOCK'
        
        row = (req_id, sec_id, start_km, end_km, 'UP' if 'UP' in sec_id else 'DOWN', 
               'PSI_TSS_AJNI', 'PSI_SP_BUTIBORI', b_type, 120 + priority * 30, win_start, win_end, 
               ",".join(def_ids), ",".join(sch_ids), 'DEP_AJNI', 'TW_8W_01', priority, 'SUBMITTED_TO_BDMS', now.strftime('%Y-%m-%d %H:%M:%S'))
        block_requests_inserted.append(row)

    cursor.executemany("INSERT INTO tdms_block_requests VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", block_requests_inserted)

    conn.commit()
    print(f"[SUCCESS] SQLite database successfully generated: '{db_path}'")

    # Export to JSON
    export_dict = {}
    for table in tables:
        cursor.execute(f"SELECT * FROM {table};")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        export_dict[table] = [dict(zip(columns, row)) for row in rows]

    with open(json_out_path, 'w', encoding='utf-8') as f:
        json.dump(export_dict, f, indent=2)
    print(f"[SUCCESS] Complete TDMS JSON dataset successfully exported: '{json_out_path}'")

    conn.close()

if __name__ == '__main__':
    generate_data()
