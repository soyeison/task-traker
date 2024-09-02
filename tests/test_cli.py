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

    # -------------------------- add -----------------------------

    def test_add(self):
        TaskDomain.add("Description test add")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][1], "Description test add")

    def test_add_id(self):
        TaskDomain.add("First description test add")
        TaskDomain.add("Second description test add")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[1][0], '2')

    def test_add_status(self):
        TaskDomain.add("Description of test")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][2], 'todo')

    def test_add_more_arguments(self):
        pass

    # -------------------------- list -----------------------------

    def test_list(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.add("Description of test number three")
        
        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][1], "Description of test number one")
            self.assertEqual(rows[1][1], "Description of test number two")
            self.assertEqual(rows[2][1], "Description of test number three")

    # -------------------------- delete -----------------------------

    def test_delete(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.add("Description of test number three")
        TaskDomain.delete("1")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(len(rows), 2)

    # -------------------------- update -----------------------------

    def test_update(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.update("1", "Description updated")

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
            self.assertEqual(rows[0][1], "Description updated")

    # -------------------------- mark status -----------------------------

    def test_list_done(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.add("Description of test number three")
        TaskDomain.markProgress('1', 'mark-done')
        TaskDomain.markProgress('3', 'mark-done')

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)

            tasksDone = []
            for task in rows:
                if task[2] == 'done':
                    tasksDone.append(task)

            self.assertEqual(len(tasksDone), 2)

    def test_list_in_progress(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.add("Description of test number three")
        TaskDomain.markProgress('1', 'mark-in-progress')
        TaskDomain.markProgress('3', 'mark-in-progress')

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)

            tasksDone = []
            for task in rows:
                if task[2] == 'in-progress':
                    tasksDone.append(task)

            self.assertEqual(len(tasksDone), 2)

    def test_list_todo(self):
        TaskDomain.add("Description of test number one")
        TaskDomain.add("Description of test number two")
        TaskDomain.add("Description of test number three")
        TaskDomain.markProgress('1', 'mark-in-progress')
        TaskDomain.markProgress('3', 'mark-in-progress')

        with open(self.fileName, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)

            tasksDone = []
            for task in rows:
                if task[2] == 'todo':
                    tasksDone.append(task)

            self.assertEqual(len(tasksDone), 1)

if __name__ == '__main__':
    unittest.main()