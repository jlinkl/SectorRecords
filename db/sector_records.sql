DROP TABLE runs;
DROP TABLE lost_sectors;
DROP TABLE runners;
DROP TABLE seasons;

CREATE TABLE lost_sectors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE runners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    num_records INT
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    link VARCHAR(255),
    runner_id INT NOT NULL REFERENCES runners(id) ON DELETE CASCADE,
    lost_sector_id INT NOT NULL REFERENCES lost_sectors(id) ON DELETE CASCADE,
    season_id INT NOT NULL REFERENCES seasons(id) ON DELETE CASCADE
);

INSERT INTO lost_sectors (name) VALUES ('Aphelions Rest'), ('Bay of Drowned Wishes'), 
('Chamber of Starlight'), ('K1 Crew Quarters'), ('K1 Logistics'), ('K1 Communion'), ('K1 Revelation'),
('Excavation Site'), ('Skydock IV'), ('The Quarry'), ('Scavengers Den'), ('Metamorphosis'), ('Sepulcher'),
('Extraction'), ('Thrilladrome'), ('Hydropponics Delta'), ('Guilded Precept'), ('The Conflux'), ('Perdition'),
('Bunker E15'), ('Concealed Void'), ('Exodus Garden 2A'), ('Veles Labyrinth');

INSERT INTO runners (name) VALUES ('Skaryton'), ('Adlayy'), ('SheckelBoi'), ('Kev'), ('Taskeren'), 
('Levie'), ('skrii'), ('Pegy16'), ('Tabbys'), ('xemo'), ('Tonal_'), ('Aoterra'), ('Suutek'), ('Barbuxx'),
('Kapuhsky'), ('Clawtivity'), ('T J'), ('INathan162'), ('Theorii'), ('Supercool666');

INSERT INTO seasons (name) VALUES ('Season of the Deep'), ('Season of Defiance'), ('Season of the Seraph'), ('Season of the Plunder'),
('Season of the Haunted'), ('Season of the Risen'), ('Season of the Lost'), ('Season of the Splicer'), ('Season of the Chosen'),
 ('Season of the Hunted');

 INSERT INTO runs ()
