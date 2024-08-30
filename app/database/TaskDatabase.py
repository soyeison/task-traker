import csv
from database.TaskModel import TaskDatabaseModel

class TaskDatabaseOperations:

    taskList: TaskDatabaseModel = []
    with open('database.csv', 'r', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for id, description, status, createdAt, updatedAt in reader:
            taskList.append(TaskDatabaseModel(id, description, status))

    @staticmethod
    def add(id, description, status):
        newTaskModel = TaskDatabaseModel(id, description, status)
        TaskDatabaseOperations.taskList.append(newTaskModel)
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
        with open('database.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for task in TaskDatabaseOperations.taskList:
                writer.writerow([task.id, task.description, task.status, task.createdAt, task.updatedAt])