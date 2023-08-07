import unittest
from models.runner import Runner

class TestRunner(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("Skaryton", 1)

#testing to see if the lost sector class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Skaryton", self.runner.name)

#testing to see if the lost sector class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.runner.id)