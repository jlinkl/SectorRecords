import unittest
from models.season import Season

class TestSeason(unittest.TestCase):
    def setUp(self):
        self.season = Season("Season of the Deep", 1)

#testing to see if the season class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Season of the Deep", self.season.name)

#testing to see if the season class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.season.id)