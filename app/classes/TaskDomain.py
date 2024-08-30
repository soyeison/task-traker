from datetime import datetime
from database.TaskDatabase import TaskDatabaseOperations
from database.TaskModel import TaskDatabaseModel

class TaskDomain:
    def __init__(self, description):
        self.description = description

    def add(self):
        initialStatus = 'todo'
        createdAt = datetime.now()
        updatedAt = datetime.now()
        newTaskDatabase = TaskDatabaseModel('1', self.description, initialStatus, createdAt, updatedAt)
        TaskDatabaseOperations.add(newTaskDatabase)

    # Modify this method to save array of dicts
    @staticmethod
    def list():
        return TaskDatabaseOperations.list()