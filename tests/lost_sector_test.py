import unittest
from models.lost_sector import LostSector 
from repositories import lost_sector_repository


class TestLostSector(unittest.TestCase):
    def setUp(self):
        self.lostsector = LostSector("Aphelions Rest", 1)
        self.lostsectors = lost_sector_repository.select_all()

#testing to see if the lost sector class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Aphelions Rest", self.lostsector.name)

#testing to see if the lost sector class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.lostsector.id)

#testing to see if the lost_sectors table holds data
    def test_table_contains_data(self):
        num_of_rows = len(self.lostsectors)
        self.assertGreater(num_of_rows, 0)