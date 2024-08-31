import os
import csv
import unittest
import config
from domain.task_domain import TaskDomain

class TestCli(unittest.TestCase):
    def setUp(self):
        self.fileName = config.DATABASE_FILE
        self.description = "Una nueva entrada para testear con unittest"

    def tearDown(self):
        # ELiminar el contenido del archivo test
        with open(self.fileName, 'w') as file:
            pass

    def test_add(self):
        newTask = TaskDomain(self.description)
        newTask.add()

        # Revisar que si se haya agregado el nuevo registro
        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][1], self.description)

if __name__ == '__main__':
    unittest.main()