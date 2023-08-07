import unittest
from models.run import Run

class TestRun(unittest.TestCase):
    def setUp(self):
        self.run = Run("test", 1, 1, 1, 1)

#testing to see if the run class correctly holds its name
    def test_class_name(self):
        self.assertEqual("test", self.run.link)

#testing to see if the run correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.run.id)

#testing to see if the run correctly holds its season id
    def test_class_seasonid(self):
        self.assertEqual(1, self.run.seasonid)
    
#testing to see if the run correctly holds its runner id
    def test_class_runnerid(self):
        self.assertEqual(1, self.run.runnerid)
    
#testing to see if the run correctly holds its lost sector id
    def test_class_lostsectorid(self):
        self.assertEqual(1, self.run.lost_sectorid)