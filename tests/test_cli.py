import os
import csv
import unittest
from domain.task_domain import TaskDomain

class TestCli(unittest.TestCase):
    def setUp(self):
        self.fileName = 'test_database.csv'
        self.description = "Una nueva entrada para testear con unittest"

    def tearDown(self):
        # ELiminar el archivo csv test
        if os.path.exists(self.fileName):
            os.remove(self.fileName)

    def add(self):
        print("Voy a ejecutar el test de add")
        TaskDomain.add()

        # Revisar que si se haya agregado el nuevo registro
        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)

        self.assertEqual(rows[0].description, self.description)

if __name__ == '__main__':
    unittest.main()