-- =============================================================================
-- TRACTION DISTRIBUTION MANAGEMENT SYSTEM (TDMS) - DATABASE SCHEMA
-- Designed for Indian Railways SIH 2026 Problem Statement: SIH26027
-- AI-Powered Automatic Block Planning Integration
-- =============================================================================

-- 1. Railway Geography & Administrative Hierarchy
CREATE TABLE IF NOT EXISTS trd_zones (
    zone_id VARCHAR(10) PRIMARY KEY, -- e.g., 'CR', 'WR', 'NR', 'SECR'
    zone_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS trd_divisions (
    division_id VARCHAR(10) PRIMARY KEY, -- e.g., 'NGP', 'BSL', 'BB'
    zone_id VARCHAR(10) REFERENCES trd_zones(zone_id),
    division_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS trd_sections (
    section_id VARCHAR(20) PRIMARY KEY, -- e.g., 'NGP-WR', 'BSL-IGP'
    division_id VARCHAR(10) REFERENCES trd_divisions(division_id),
    section_name VARCHAR(100) NOT NULL,
    start_km DECIMAL(8,3) NOT NULL,
    end_km DECIMAL(8,3) NOT NULL,
    line_type VARCHAR(20) CHECK (line_type IN ('UP', 'DOWN', 'THIRD', 'FOURTH', 'YARD', 'BYPASS')),
    electrified_voltage_kv DECIMAL(4,1) DEFAULT 25.0 -- 25 kV AC or 2x25 kV
);

-- 2. Power Supply Installations (PSI Master Assets)
CREATE TABLE IF NOT EXISTS psi_installations (
    installation_id VARCHAR(30) PRIMARY KEY, -- e.g., 'TSS_AJNI', 'SP_BUTIBORI'
    section_id VARCHAR(20) REFERENCES trd_sections(section_id),
    installation_type VARCHAR(20) CHECK (installation_type IN ('TSS', 'SP', 'SSP', 'FP')), -- Traction Substation, Sectioning Post, Sub-Sectioning Post, Feeding Post
    location_km DECIMAL(8,3) NOT NULL,
    grid_supply_voltage_kv DECIMAL(5,1) DEFAULT 132.0, -- 132kV / 220kV grid input
    num_transformers INT DEFAULT 2,
    scada_enabled BOOLEAN DEFAULT TRUE,
    operational_status VARCHAR(20) DEFAULT 'ACTIVE'
);

-- 3. Overhead Equipment (OHE Assets)
CREATE TABLE IF NOT EXISTS ohe_masts (
    mast_id VARCHAR(40) PRIMARY KEY, -- e.g., 'NGP-WR_UP_245/12'
    section_id VARCHAR(20) REFERENCES trd_sections(section_id),
    location_km DECIMAL(8,3) NOT NULL,
    mast_number VARCHAR(20) NOT NULL, -- e.g., '245/12'
    track_line VARCHAR(10) NOT NULL, -- 'UP', 'DOWN'
    structure_type VARCHAR(30), -- 'Portal', 'Single Mast', 'TTC', 'Cantilever'
    catenary_wire_type VARCHAR(50) DEFAULT '65 sq.mm Cadmium Copper',
    contact_wire_type VARCHAR(50) DEFAULT '107 sq.mm Hard Drawn Copper',
    stagger_mm INT,
    height_meters DECIMAL(4,2) DEFAULT 5.50,
    installation_date DATE
);

-- 4. Maintenance Resource Assets (Tower Wagons & TRD Depots)
CREATE TABLE IF NOT EXISTS trd_depots (
    depot_id VARCHAR(20) PRIMARY KEY, -- e.g., 'DEP_NGP', 'DEP_WR'
    division_id VARCHAR(10) REFERENCES trd_divisions(division_id),
    depot_name VARCHAR(100) NOT NULL,
    location_station VARCHAR(50) NOT NULL,
    contact_number VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS tower_wagons (
    tw_id VARCHAR(20) PRIMARY KEY, -- e.g., 'TW_8W_001'
    depot_id VARCHAR(20) REFERENCES trd_depots(depot_id),
    tw_code VARCHAR(30) UNIQUE NOT NULL, -- e.g., '8W-NETRA-04'
    tw_type VARCHAR(20) CHECK (tw_type IN ('4-WHEELER', '8-WHEELER', 'NETRA_SPECIAL')),
    max_speed_kmph INT DEFAULT 110,
    operational_status VARCHAR(20) DEFAULT 'AVAILABLE', -- 'AVAILABLE', 'UNDER_MAINTENANCE', 'DEPLOYED'
    last_fitness_cert_date DATE
);

-- 5. TRD Defect Logging System (Core feed for Block Planner)
CREATE TABLE IF NOT EXISTS tdms_defects (
    defect_id VARCHAR(40) PRIMARY KEY, -- e.g., 'DEF_TRD_2026_001'
    section_id VARCHAR(20) REFERENCES trd_sections(section_id),
    mast_id VARCHAR(40) REFERENCES ohe_masts(mast_id),
    installation_id VARCHAR(30) REFERENCES psi_installations(installation_id),
    subsystem VARCHAR(30) CHECK (subsystem IN ('OHE', 'PSI', 'SCADA', 'BONDING', 'TOWER_WAGON')),
    defect_category VARCHAR(50) NOT NULL, -- e.g., 'Contact Wire Wear', 'Insulator Flashover', 'Cantilever Misalignment', 'Bird Nest Near Live Wire', 'Hotspot in Isolator'
    severity VARCHAR(10) CHECK (severity IN ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW')), -- CRITICAL requires immediate Emergency Block
    detected_by VARCHAR(50), -- 'Foot Patrol', 'Cab Inspection', 'Thermovision NETRA', 'SCADA Trip'
    detection_date TIMESTAMP NOT NULL,
    target_rectification_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'OPEN' CHECK (status IN ('OPEN', 'BLOCK_REQUESTED', 'BLOCK_APPROVED', 'RESOLVED', 'DEFERRED')),
    power_block_required BOOLEAN DEFAULT TRUE,
    traffic_block_required BOOLEAN DEFAULT FALSE,
    estimated_work_duration_minutes INT NOT NULL, -- Minimum block duration required
    required_manpower INT DEFAULT 4,
    tower_wagon_required BOOLEAN DEFAULT TRUE,
    description TEXT
);

-- 6. Preventive Maintenance Schedules & Overdue Tracking
CREATE TABLE IF NOT EXISTS tdms_maintenance_schedules (
    schedule_id VARCHAR(40) PRIMARY KEY,
    section_id VARCHAR(20) REFERENCES trd_sections(section_id),
    asset_type VARCHAR(30) CHECK (asset_type IN ('OHE_SPAN', 'TSS_TRANSFORMER', 'CIRCUIT_BREAKER', 'ISOLATOR', 'AT_TRANSFORMER', 'NEUTRAL_SECTION')),
    asset_id VARCHAR(40) NOT NULL,
    maintenance_type VARCHAR(30) CHECK (maintenance_type IN ('MONTHLY', 'QUARTERLY', 'HALF_YEARLY', 'ANNUAL', 'IOH', 'POH')),
    last_done_date DATE NOT NULL,
    due_date DATE NOT NULL,
    overdue_days INT GENERATED ALWAYS AS (MAX(0, CURRENT_DATE - due_date)) STORED,
    urgency_score DECIMAL(5,2) DEFAULT 0.0, -- Computed score for AI Block Planner priority
    estimated_duration_minutes INT NOT NULL,
    power_block_required BOOLEAN DEFAULT TRUE,
    traffic_block_required BOOLEAN DEFAULT FALSE,
    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'SCHEDULED', 'COMPLETED', 'OVERDUE'))
);

-- 7. Power Block Requests (Payload generated by TDMS for BDMS/COA Integration)
CREATE TABLE IF NOT EXISTS tdms_block_requests (
    block_request_id VARCHAR(40) PRIMARY KEY, -- e.g., 'PBR_TRD_2026_104'
    section_id VARCHAR(20) REFERENCES trd_sections(section_id),
    start_km DECIMAL(8,3) NOT NULL,
    end_km DECIMAL(8,3) NOT NULL,
    track_line VARCHAR(10) CHECK (track_line IN ('UP', 'DOWN', 'BOTH', 'YARD')),
    isolation_post_from VARCHAR(30) REFERENCES psi_installations(installation_id),
    isolation_post_to VARCHAR(30) REFERENCES psi_installations(installation_id),
    block_type VARCHAR(30) CHECK (block_type IN ('POWER_BLOCK', 'TRAFFIC_AND_POWER_BLOCK', 'SHADOW_BLOCK', 'EMERGENCY_POWER_BLOCK')),
    requested_duration_minutes INT NOT NULL,
    preferred_window_start TIMESTAMP,
    preferred_window_end TIMESTAMP,
    associated_defect_ids TEXT, -- Comma-separated or JSON list of defect IDs bundled into this block request
    associated_schedule_ids TEXT, -- Comma-separated or JSON list of routine maintenance schedules
    depot_id VARCHAR(20) REFERENCES trd_depots(depot_id),
    assigned_tw_id VARCHAR(20) REFERENCES tower_wagons(tw_id),
    priority_level INT CHECK (priority_level BETWEEN 1 AND 5), -- 1 = Emergency, 5 = Routine
    status VARCHAR(30) DEFAULT 'SUBMITTED_TO_BDMS' CHECK (status IN ('DRAFT', 'SUBMITTED_TO_BDMS', 'COA_OPTIMIZED', 'APPROVED', 'REJECTED', 'EXECUTED', 'CANCELLED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 8. SCADA Live Telemetry & Trip Logs
CREATE TABLE IF NOT EXISTS tdms_scada_trips (
    trip_id VARCHAR(40) PRIMARY KEY,
    installation_id VARCHAR(30) REFERENCES psi_installations(installation_id),
    feeder_name VARCHAR(50) NOT NULL,
    trip_timestamp TIMESTAMP NOT NULL,
    fault_current_amps INT,
    fault_distance_km DECIMAL(8,3),
    auto_reclosed BOOLEAN DEFAULT FALSE,
    tripping_reason VARCHAR(100), -- 'Distance Protection Trip', 'Overcurrent Trip', 'PT Breakage', 'Transient Snap'
    associated_defect_id VARCHAR(40) REFERENCES tdms_defects(defect_id)
);
