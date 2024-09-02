import csv
import config
from database.task_model import TaskDatabaseModel
from errors.write_csv_file_exception import WriteCsvFileException
from errors.dont_exist_task_id import DontExistTaskId

class TaskDatabaseOperations:

    taskList: TaskDatabaseModel = []

    try:
        with open(config.DATABASE_FILE, 'r', newline='\n') as fichero:
                reader = csv.reader(fichero, delimiter=';')
                for id, description, status, createdAt, updatedAt in reader:
                    taskList.append(TaskDatabaseModel(id, description, status, createdAt, updatedAt))
    except ValueError as e:
        print(f"Problems trying read elements from database: {e}")

    @staticmethod
    def add(task: TaskDatabaseModel):
        TaskDatabaseOperations.taskList.append(task)
        TaskDatabaseOperations.save()

    @staticmethod
    def list(filter = None):
        if filter is None:
            return TaskDatabaseOperations.taskList
        else:
            listToSend = []
            for task in TaskDatabaseOperations.taskList:
                if task.status == filter:
                    listToSend.append(task)
            return listToSend

    
    @staticmethod
    def delete(id):
        task = None
        for index, task in enumerate(TaskDatabaseOperations.taskList):
            if task.id == id:
                task = TaskDatabaseOperations.taskList.pop(index)
                TaskDatabaseOperations.save()

        if task is None:
            raise DontExistTaskId(f"Don't exist task with id: {id}")
        return task

    @staticmethod
    def update(id, attributeType, attributeValue):
        task = None
        for i in range(len(TaskDatabaseOperations.taskList)):
            if TaskDatabaseOperations.taskList[i].id == id:
                task = TaskDatabaseOperations.taskList[i]
                setattr(TaskDatabaseOperations.taskList[i], attributeType, attributeValue)
                TaskDatabaseOperations.save()

        if task is None:
            raise DontExistTaskId(f"Don't exist task with id: {id}")
        return task

    @staticmethod
    def save():
        try:
            with open(config.DATABASE_FILE, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for task in TaskDatabaseOperations.taskList:
                    writer.writerow([task.id, task.description, task.status, task.createdAt, task.updatedAt])
        except IOError as e:
            raise WriteCsvFileException(f"Error writting in CSV: {e}")