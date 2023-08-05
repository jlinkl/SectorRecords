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
    name VARCHAR(255)
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
('Bunker E15'), ('Concealed Void'), ('Exodus Garden 2A'), ('Veles Labyrinth'), ('Empty Tank');

INSERT INTO runners (name) VALUES ('Skaryton'), ('Adlayy'), ('SheckelBoi'), ('Kev'), ('Taskeren'), 
('Levie'), ('skrii'), ('Pegy16'), ('Tabbys'), ('xemo'), ('Tonal_'), ('Aoterra'), ('Suutek'), ('Barbuxx'),
('Kapuhsky'), ('Clawtivity'), ('T J'), ('INathan162'), ('Theorii'), ('Supercool666'), ('notpebis'), ('alexpariente06');

INSERT INTO seasons (name) VALUES ('Season of the Deep'), ('Season of Defiance'), ('Season of the Seraph'), ('Season of the Plunder'),
('Season of the Haunted'), ('Season of the Risen'), ('Season of the Lost'), ('Season of the Splicer'), ('Season of the Chosen'),
 ('Season of the Hunted');

 INSERT INTO runs (link, runner_id, lost_sector_id, season_id) VALUES ('https://youtu.be/FZwf071gPuY', 1, 1, 1), ('https://youtu.be/vMkDqtVXkxU', 1, 1, 2),
 ('https://youtu.be/imNFmSHqHbI', 6, 1, 3), ('https://youtu.be/2P5mwSu4hTU', 6, 1, 6), ('https://youtu.be/5-RKIxH0znE', 16, 1 , 7),
 ('https://youtu.be/2e5f19OLDKQ', 1, 2, 1), ('https://youtu.be/oUe4d0HiZ_U', 12, 2, 6), ('https://youtu.be/78DrO-eFnfQ', 12, 2, 7),
 ('https://youtu.be/j-V6pbkDISk', 1, 3, 1), ('https://youtu.be/-XVCcjzsu-U', 4, 3, 2), ('https://youtu.be/1X2KycPmSbs', 1, 3, 3), ('https://youtu.be/h019tcW4LZg', 6, 3, 6),
 ('https://youtu.be/sdt8Fw76Frw', 1, 3, 7), ('https://youtu.be/dEHxkUK5kEU', 2, 4, 1), ('https://youtu.be/ExMSGZ29-lw', 1, 4, 3), ('https://youtu.be/GIFVg4kqnEM', 1, 4, 4),
 ('https://youtu.be/tb0td8--l5w', 1, 4, 5), ('https://youtu.be/y4_wyt-41oU', 2, 4, 6), ('https://youtu.be/MtNeLxjrBm8', 1, 4, 7), ('https://youtu.be/1ZOF__ohsKk', 1, 4, 8),
 ('https://youtu.be/MpscJDX7e80', 2, 4, 9), ('https://youtu.be/WZl2HOddQ7g', 2, 5, 1), ('https://youtu.be/UcNwzS1ljUg', 6, 5, 3), ('https://youtu.be/Nv8FRoc4tgo', 6, 5, 4),
 ('https://youtu.be/oS4_VbYuiSs', 6, 5, 5), ('uavailable', 17, 5, 7), ('https://youtu.be/e6i7CIB0rgQ', 1, 5, 8), ('https://youtu.be/UKF1HgyYp8w', 1, 5, 9),
 ('https://youtu.be/mg01VSPP5Lk', 2, 6, 1), ('https://youtu.be/mPc6SdJjmC4', 1, 6, 3), ('https://youtu.be/tWV1husIsNs', 1, 6, 4), ('https://youtu.be/zyibCKxWLxo', 1, 6, 5),
 ('https://youtu.be/67-yS5onULY', 1, 6, 6), ('https://youtu.be/xnVgkKeDPaQ', 1, 6, 7), ('https://youtu.be/W3tE-pyRirQ', 2, 6, 8), ('https://youtu.be/YAEidEJfDh8', 1, 6, 9),
 ('https://youtu.be/SVsqCKFAfFc', 2, 7, 1), ('https://youtu.be/YRWd2JeBa5A', 1, 7, 3), ('https://youtu.be/udOwxID3WIs', 1, 7, 5), ('https://youtu.be/l3nuw3tmrv0', 1, 7, 6),
 ('https://youtu.be/nsh4H-MHz-8', 1, 7, 7), ('https://youtu.be/zh8EH3pELIU', 1, 7, 8), ('https://youtu.be/ID7AG5r4pNo', 1, 7, 9), ('https://youtu.be/rY57hMX7Pec', 21, 8, 2),
 ('https://youtu.be/nGmKpFsrSQs', 1, 8, 4), ('https://youtu.be/56xUlx_ahD0', 1, 8, 5), ('https://youtu.be/SU3QugIdf7E', 12, 8, 8), ('https://youtu.be/VrhrvvxbJXw', 3, 9, 2), 
 ('https://youtu.be/ypdgpMujkLA', 6, 9, 4), ('https://youtu.be/E33BaBJTn9c', 9, 9, 5), ('https://youtu.be/I-bF-KYlPCo', 1, 9, 5), ('https://youtu.be/ynNJL976B2w', 22, 9, 6),  
 ('https://youtu.be/sP0RW8FESI8', 4, 10, 2), ('https://youtu.be/CL_qgmupLFw', 1, 10, 4), ('https://youtu.be/2YHZNTxXy30', 10, 10, 5), ('https://youtu.be/VKxXF5UcQcQ', 1, 10, 8),
 ('https://youtu.be/I-RxR11w9_0', 1, 11, 4), ('https://youtu.be/9dhBSr0-jvM', 1, 11, 8), ('https://youtu.be/USwLu6yfdUM', 1, 12, 5), ('https://youtu.be/lM02W8x0ITg', 13, 12, 6), 
 ('https://youtu.be/CE9B_nVFy6U', 1, 12, 6), ('https://youtu.be/ISgrONPXkOE', 2, 12, 1), ('https://youtu.be/jbAIdHJhky0', 1, 12, 3), ('https://youtu.be/RmcYnGUxY3E', 6, 12, 5), 
 ('https://youtu.be/TqyXrAd2DZM', 6, 12, 6), ('https://youtu.be/YbF-Ucv7VfM', 3, 13, 1), ('https://youtu.be/YbF-Ucv7VfM', 7, 13, 3), ('https://youtu.be/HYuW-_TL2OI', 11, 13, 5), 
 ('https://youtu.be/YGY3aTHkabk', 1, 13, 6), ('https://youtu.be/aPjs6S9-3Xg', 5, 17, 2), ('https://youtu.be/Z5eAsmONdoY', 6, 18, 4), ('https://youtu.be/QL5TSgVy3R8', 1, 18, 5), 
 ('https://youtu.be/pVdsK0BdLpw', 4, 19, 2), ('https://youtu.be/qZNSAHwn29w', 1, 19, 3), ('https://youtu.be/5WzaqB9WjC8', 8, 19, 4), ('https://youtu.be/WAvjAqYVyJU', 1, 19, 7), 
 ('https://youtu.be/cbeC3hUWchU', 1, 19, 8), ('https://youtu.be/0AW5d70vUno', 1, 19, 9), ('https://youtu.be/DjlI7Bdex1o', 1, 20, 3), ('https://youtu.be/nzpEvYFCJ0s', 1, 20, 4), 
 ('https://youtu.be/mctIE-Z5dwg', 1, 20, 7), ('https://youtu.be/uL2UHlWwZqM', 1, 20, 8), ('https://youtu.be/mVxRrcbT9SM', 2, 20, 9), ('https://youtu.be/obGdIIs6xxI', 2, 20, 10), 
 ('https://youtu.be/baYv6WfNJI8', 1, 21, 3), ('https://youtu.be/YHtMD73XXac', 1, 21, 4), ('https://youtu.be/1i-dyskv8jY', 1, 21, 7), ('https://youtu.be/l0HpFU4f9s8', 15, 21, 8), 
('https://youtu.be/qvhqA4pIUUU', 1, 21, 9), ('https://youtu.be/crlEYhaSXA4', 1, 21, 10), ('https://youtu.be/P1HAZu1kMd0', 2, 22, 1), ('https://youtu.be/S-fYvG82Mms', 6, 22, 6), 
('https://youtu.be/NCHbcAPuFAs', 1, 22, 8), ('https://youtu.be/76liYX_3nH4', 2, 22, 9), ('https://youtu.be/_H8fyNKLCbU', 20, 22, 10), ('https://youtu.be/nO5m_HKH6QU', 2, 23, 1), 
('https://youtu.be/JcOQ3vPW-Ko', 2, 23, 6), ('https://youtu.be/bCIzbMY9yFE', 18, 23, 8), ('https://youtu.be/jaldxk2tRZE', 18, 23, 9), ('https://youtu.be/nVDAzbSbalk', 19, 23, 10), 
('https://youtu.be/ALkyyiLPZxE', 14, 24, 7), ('https://youtu.be/Qv0z6Nvzk6g', 15, 24, 8)