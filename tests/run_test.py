import unittest
from models.run import Run
from repositories import run_repository
from db import run_sql

class TestRun(unittest.TestCase):
    def setUp(self):
        run_sql.reset_tables()
        self.run = Run("test", 1, 1, 1, 1)
        self.runs = run_repository.select_all()

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
    
#testing to see if the runs table holds data
    def test_table_contains_data(self):
        num_of_rows = len(self.runs)
        self.assertGreater(num_of_rows, 0)

#testing to see if i can find a runs given its id
    def test_find_run(self):
        found_run = run_repository.find(2)
        self.assertEqual(found_run.link, "https://youtu.be/vMkDqtVXkxU")

#testing to see if i can add a run to the db
    def test_add_run(self):
        run = Run("test", 1, 1, 1, 0)
        run_repository.add(run)
        self.assertGreater(len(run_repository.select_all()), len(self.runs))

#testing to see if i can change the data of a run, given its id
    def test_change_run(self):
        run = Run('test', 1, 1, 1, 1)
        run_repository.update(run)
        self.assertEqual(run.link, run_repository.find(1).link)

#testing to see if i can delete a run entry from the table, given its id
    def test_delete_run(self):
        run_repository.add(Run("test", 1, 1, 1, 0))
        run_repository.delete(len(self.runs))
        self.assertEqual(len(self.runs), len(run_repository.select_all()))