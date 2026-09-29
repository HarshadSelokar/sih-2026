-- =============================================================================
-- INDIAN RAILWAYS COMPREHENSIVE DATASET SCHEMA FOR SIH 26027
-- Integrates COA (Train Schedules), TMS (Track Schedules), Real-Time Tracking & Rescheduling
-- =============================================================================

-- 1. COA TRAIN SCHEDULES MASTER DATA
CREATE TABLE IF NOT EXISTS trains (
    train_number VARCHAR(10) PRIMARY KEY, -- e.g., '20912', '12105', 'GOODS_CONTAINER_01'
    train_name VARCHAR(100) NOT NULL,
    train_type VARCHAR(30) CHECK (train_type IN ('VANDE_BHARAT', 'RAJDHANI', 'SUPERFAST', 'EXPRESS', 'PASSENGER', 'FREIGHT_CONTAINER', 'FREIGHT_COAL', 'FREIGHT_RAKE')),
    priority_rank INT NOT NULL, -- 1 = Highest (Vande Bharat), 10 = Freight
    origin_station VARCHAR(50) NOT NULL,
    destination_station VARCHAR(50) NOT NULL,
    max_permissible_speed_kmph INT DEFAULT 130,
    rake_length_coaches_or_wagons INT DEFAULT 22,
    loco_type VARCHAR(20) DEFAULT 'WAP-7'
);

CREATE TABLE IF NOT EXISTS train_schedule_routes (
    schedule_id VARCHAR(40) PRIMARY KEY,
    train_number VARCHAR(10) REFERENCES trains(train_number),
    section_id VARCHAR(20) NOT NULL, -- e.g., 'SEC_NGP_WR_UP'
    sequence_no INT NOT NULL,
    station_code VARCHAR(10), -- Station if halt, NULL if section passing
    scheduled_arrival TIMESTAMP,
    scheduled_departure TIMESTAMP,
    dwell_minutes INT DEFAULT 0,
    entry_km DECIMAL(8,3) NOT NULL,
    exit_km DECIMAL(8,3) NOT NULL,
    scheduled_speed_kmph INT DEFAULT 110
);

-- 2. TMS TRACK SCHEDULES & CORRIDOR CONDITION DATA
CREATE TABLE IF NOT EXISTS track_corridor_assets (
    track_id VARCHAR(40) PRIMARY KEY,
    section_id VARCHAR(20) NOT NULL,
    track_line VARCHAR(10) CHECK (track_line IN ('UP', 'DOWN', 'THIRD', 'FOURTH', 'YARD')),
    start_km DECIMAL(8,3) NOT NULL,
    end_km DECIMAL(8,3) NOT NULL,
    rail_weight_kg VARCHAR(20) DEFAULT '60kg 90UTS',
    sleeper_density INT DEFAULT 1660, -- sleepers per km
    ballast_cushion_mm INT DEFAULT 350,
    tgi_score DECIMAL(5,2) DEFAULT 75.0, -- Track Geometry Index (Lower = Poor)
    last_tamping_date DATE,
    last_deep_screening_date DATE
);

CREATE TABLE IF NOT EXISTS tms_track_schedules (
    track_schedule_id VARCHAR(40) PRIMARY KEY,
    section_id VARCHAR(20) NOT NULL,
    start_km DECIMAL(8,3) NOT NULL,
    end_km DECIMAL(8,3) NOT NULL,
    maintenance_activity VARCHAR(100) NOT NULL, -- 'BCM Deep Screening', 'Tamping with CSM', 'Rail Renewal (TRR)', 'Weld Testing'
    track_block_duration_minutes INT NOT NULL,
    required_machinery VARCHAR(100), -- 'CSM Tamper Machine + DGS', 'BCM Machine'
    urgency_level VARCHAR(20) CHECK (urgency_level IN ('CRITICAL', 'HIGH', 'MEDIUM', 'ROUTINE')),
    planned_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'PLANNED' CHECK (status IN ('PLANNED', 'REQUESTED', 'APPROVED', 'COMPLETED'))
);

CREATE TABLE IF NOT EXISTS temporary_speed_restrictions (
    tsr_id VARCHAR(40) PRIMARY KEY,
    section_id VARCHAR(20) NOT NULL,
    start_km DECIMAL(8,3) NOT NULL,
    end_km DECIMAL(8,3) NOT NULL,
    restricted_speed_kmph INT NOT NULL, -- e.g., 30 kmph restriction
    normal_speed_kmph INT DEFAULT 130,
    reason VARCHAR(150) NOT NULL, -- 'Weak embankment', 'Track realignment work', 'Hot weather precaution'
    issued_date DATE NOT NULL,
    expected_removal_date DATE
);

-- 3. REAL-TIME TRAIN TRACKING DATA (COA / NTES LIVE STREAM)
CREATE TABLE IF NOT EXISTS realtime_train_tracking (
    tracking_id VARCHAR(50) PRIMARY KEY,
    train_number VARCHAR(10) REFERENCES trains(train_number),
    current_section_id VARCHAR(20) NOT NULL,
    current_km_location DECIMAL(8,3) NOT NULL,
    current_speed_kmph INT NOT NULL,
    delay_minutes INT DEFAULT 0, -- +mins late, negative = early
    running_status VARCHAR(30) CHECK (running_status IN ('RUNNING_ON_TIME', 'RUNNING_LATE', 'DETAINED_AT_SIGNAL', 'REGULATED_AT_STATION', 'WAITING_FOR_BLOCK')),
    occupancy_block_section VARCHAR(50), -- e.g., 'BLK_NGP_SNI_04'
    next_signal_aspect VARCHAR(20) CHECK (next_signal_aspect IN ('GREEN', 'DOUBLE_YELLOW', 'YELLOW', 'RED')),
    last_gps_telemetry_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. RESCHEDULING & DISRUPTION EVENTS DATA
CREATE TABLE IF NOT EXISTS train_rescheduling_events (
    reschedule_id VARCHAR(40) PRIMARY KEY,
    train_number VARCHAR(10) REFERENCES trains(train_number),
    original_departure_time TIMESTAMP NOT NULL,
    rescheduled_departure_time TIMESTAMP NOT NULL,
    delay_offset_minutes INT NOT NULL,
    cause_category VARCHAR(50) CHECK (cause_category IN ('POWER_BLOCK_MAINTENANCE', 'TRACK_MAINTENANCE', 'SIGNAL_FAILURE', 'LOCO_FAILURE', 'ACCIDENT_DERAILMENT', 'WEATHER_FOG')),
    reschedule_reason TEXT NOT NULL,
    regulation_station VARCHAR(50), -- Station where train is held to allow block
    action_type VARCHAR(30) CHECK (action_type IN ('RETIMED', 'REGULATED', 'DIVERTED', 'SHORT_TERMINATED', 'CANCELLED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
