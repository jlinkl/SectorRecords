import unittest
from models.lost_sector import LostSector

class TestLostSector(unittest.TestCase):
    def setUp(self):
        self.lostsector = LostSector("Aphelions Rest", 1)

#testing to see if the lost sector class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Aphelions Rest", self.lostsector.name)

#testing to see if the lost sector class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.lostsector.id)