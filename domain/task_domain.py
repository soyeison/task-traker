from datetime import datetime
from database.task_database import TaskDatabaseOperations
from database.task_model import TaskDatabaseModel
from utils.calculate_next_id import calculate_next_id
from errors.write_csv_file_exception import WriteCsvFileException

class TaskDomain:
    @staticmethod
    def add(description):
        initialStatus = 'todo'
        createdAt = datetime.now()
        updatedAt = datetime.now()
        idToSave = calculate_next_id()
        newTaskDatabase = TaskDatabaseModel(idToSave, description, initialStatus, createdAt, updatedAt)
        try:
            TaskDatabaseOperations.add(newTaskDatabase)
        except WriteCsvFileException as e:
            raise e
        return idToSave

    # Modify this method to save array of dicts
    @staticmethod
    def list():
        return TaskDatabaseOperations.list()
    
    @staticmethod
    def delete(id):
        return TaskDatabaseOperations.delete(str(id))