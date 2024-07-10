CREATE TABLE IF NOT EXISTS algolia_output (
    id SERIAL PRIMARY KEY,
    application_id VARCHAR(255) NOT NULL,
    index_prefix VARCHAR(255) NOT NULL,
    has_specific_prefix BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);