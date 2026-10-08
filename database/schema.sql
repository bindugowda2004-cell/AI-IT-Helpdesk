-- ============================================
-- AI IT HELPDESK DATABASE
-- ============================================

-- Employees table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    employee_type VARCHAR(50)
);

-- IT support tickets
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(employee_id),
    subject VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(50),
    priority VARCHAR(20),
    status VARCHAR(30) DEFAULT 'Open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,
    resolution_time_hours DECIMAL(10,2)
);

-- Knowledge base / solutions
CREATE TABLE solutions (
    solution_id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    problem TEXT NOT NULL,
    solution TEXT NOT NULL
);

-- Machine learning predictions
CREATE TABLE predictions (
    prediction_id SERIAL PRIMARY KEY,
    ticket_id INT REFERENCES tickets(ticket_id),
    predicted_category VARCHAR(50),
    predicted_priority VARCHAR(20),
    confidence DECIMAL(5,4),
    model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AI/user interactions
CREATE TABLE interactions (
    interaction_id SERIAL PRIMARY KEY,
    ticket_id INT REFERENCES tickets(ticket_id),
    question TEXT NOT NULL,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);