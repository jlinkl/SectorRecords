import unittest
from models.runner import Runner
from repositories import runner_repository
from db import run_sql

class TestRunner(unittest.TestCase):
    def setUp(self):
        run_sql.reset_tables()
        self.runner = Runner("Skaryton", 1)
        self.runners = runner_repository.select_all()


#testing to see if the runner class correctly holds its name
    def test_class_name(self):
        self.assertEqual("Skaryton", self.runner.name)

#testing to see if the runner class correctly holds its id
    def test_class_id(self):
        self.assertEqual(1, self.runner.id)

#testing to see if the runners table holds data
    def test_table_contains_data(self):
        num_of_rows = len(self.runners)
        self.assertGreater(num_of_rows, 0)

#testing to see if i can find a runner given their id
    def test_find_runner(self):
        found_runner = runner_repository.find(2)
        self.assertEqual(found_runner.name, "Adlayy")

#testing to see if i can add a runnerto the db
    def test_add_runner(self):
        runner = Runner("test", 0)
        runner_repository.add(runner)
        self.assertGreater(len(runner_repository.select_all()), len(self.runners))

#testing to see if i can change the data of a runner, given their id
    def test_change_runner(self):
        runner = Runner('test', 1)
        runner_repository.update(runner)
        self.assertEqual(runner.name, runner_repository.find(1).name)

#testing to see if i can delete a runner entry from the table, given their id
    def test_delete_runner(self):
        runner_repository.add(Runner("test", 0))
        runner_repository.delete(23)
        self.assertEqual(len(self.runners), len(runner_repository.select_all()))