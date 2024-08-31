import csv
import config
from database.task_model import TaskDatabaseModel
from errors.write_csv_file_exception import WriteCsvFileException

class TaskDatabaseOperations:

    taskList: TaskDatabaseModel = []

    try:
        with open(config.DATABASE_FILE, 'r', newline='\n') as fichero:
                reader = csv.reader(fichero, delimiter=';')
                for id, description, status, createdAt, updatedAt in reader:
                    taskList.append(TaskDatabaseModel(id, description, status, createdAt, updatedAt))
    except ValueError as e:
        print(f"Problema en la lectura de elementos: {e}")

    @staticmethod
    def add(task: TaskDatabaseModel):
        TaskDatabaseOperations.taskList.append(task)
        TaskDatabaseOperations.save()

    @staticmethod
    def list():
        listToSend = []
        for task in TaskDatabaseOperations.taskList:
            listToSend.append(task)
        return listToSend
    
    @staticmethod
    def delete(id):
        task = None
        for i in range(len(TaskDatabaseOperations.taskList)):
            if TaskDatabaseOperations.taskList[i].id == id:
                task = TaskDatabaseOperations.taskList[i]
                TaskDatabaseOperations.taskList = TaskDatabaseOperations.taskList[0:i] + TaskDatabaseOperations.taskList[i + 1:]
                TaskDatabaseOperations.save()

        if task is None:
            return f'No se encontro la tarea con id: {id}'
        return task

    @staticmethod
    def update(id, description):
        task = None
        for i in range(len(TaskDatabaseOperations.taskList)):
            if TaskDatabaseOperations.taskList[i].id == id:
                task = TaskDatabaseOperations.taskList[i]
                TaskDatabaseOperations.taskList[i].description = description
                TaskDatabaseOperations.save()

        if task is None:
            return f'No se encontro la tarea con id: {id}'
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