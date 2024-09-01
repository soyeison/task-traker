import csv
import unittest
import config
from domain.task_domain import TaskDomain
from database.task_database import TaskDatabaseOperations

class TestCli(unittest.TestCase):
    def setUp(self):
        self.fileName = config.DATABASE_FILE

    def tearDown(self):
        TaskDatabaseOperations.taskList = []
        with open(self.fileName, 'w') as archivo:
            pass

    def test_add(self):
        TaskDomain.add("Descripcion del test add")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][1], "Descripcion del test add")

    def test_add_id(self):
        TaskDomain.add("Primera descripcion del test add")
        TaskDomain.add("Segunda descripcion del test add")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[1][0], '2')

    def test_add_status(self):
        TaskDomain.add("Descripcion del test")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][2], 'todo')

if __name__ == '__main__':
    unittest.main()