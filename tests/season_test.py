import unittest
from models.season import Season
from repositories import season_repository
from db import run_sql

class TestSeason(unittest.TestCase):
    def setUp(self):
        run_sql.reset_tables()
        self.season = Season("Season of the Deep", 1)
        self.seasons = season_repository.select_all()

#testing to see if the season class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Season of the Deep", self.season.name)

#testing to see if the season class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.season.id)

#testing to see if the seasons table holds data
    def test_table_contains_data(self):
        num_of_rows = len(self.seasons)
        self.assertGreater(num_of_rows, 0)

#testing to see if i can find a seasons given its id
    def test_find_season(self):
        found_season = season_repository.find(2)
        self.assertEqual(found_season.name, "Season of Defiance")

#testing to see if i can add a season to the db
    def test_add_season(self):
        season = Season("test", 0)
        season_repository.add(season)
        self.assertGreater(len(season_repository.select_all()), len(self.seasons))

#testing to see if i can change the data of a season, given its id
    def test_change_lost_sector(self):
        season = Season('test', 1)
        season_repository.update(season)
        self.assertEqual(season.name, season_repository.find(1).name)

#testing to see if i can delete a season entry from the table, given its id
    def test_delete_lost_sector(self):
        season_repository.add(Season("test", 0))
        season_repository.delete(len(self.seasons))
        self.assertEqual(len(self.seasons), len(season_repository.select_all()))