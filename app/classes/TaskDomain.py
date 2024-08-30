from datetime import datetime
from database.TaskDatabase import TaskDatabaseOperations
from database.TaskModel import TaskDatabaseModel
from errors.WriteCsvFileException import WriteCsvFileException

class TaskDomain:
    def __init__(self, description):
        self.description = description

    def add(self):
        initialStatus = 'todo'
        createdAt = datetime.now()
        updatedAt = datetime.now()
        newTaskDatabase = TaskDatabaseModel('1', self.description, initialStatus, createdAt, updatedAt)
        try:
            TaskDatabaseOperations.add(newTaskDatabase)
        except WriteCsvFileException as e:
            raise e

    # Modify this method to save array of dicts
    @staticmethod
    def list():
        return TaskDatabaseOperations.list()