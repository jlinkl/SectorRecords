DROP TABLE lostsectors;
DROP TABLE seasons;
DROP TABLE runners;
DROP TABLE runs;

CREATE TABLE lostsectors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE runners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    num_records INT
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    link VARCHAR(255),
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,
    lost_sector_id INT NOT NULL REFERENCES lostsectors(id) ON DELETE CASCADE,
    season_id INT NOT NULL REFERENCES seasons(id) ON DELETE CASCADE
);