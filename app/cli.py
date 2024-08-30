import argparse
from database.TaskDatabase import TaskDatabaseOperations
from database.TaskModel import TaskDatabaseModel
from classes.TaskDomain import TaskDomain

def main():
    parser = argparse.ArgumentParser(description="Manage your tasks CLI")

    parser.add_argument('operation', choices=['add', 'list', 'update', 'delete', 'mark-in-progress', 'mark-done'], help="Available operations")
    parser.add_argument('datos', type=str, nargs='*')

    args = parser.parse_args()

    if args.operation == 'add':
        newTask = TaskDomain(args.datos[1])
        newTask.add()
    elif args.operation == 'list':
        for task in TaskDomain.list():
            print(task)


    # Ejecucion del codigo
    # newTask1 = TaskDatabaseModel(1, 'Primera tarea test', 'in-progress')
    # TaskDatabaseOperations.add(newTask1.id, newTask1.description, newTask1.status)
    # newTask2 = TaskDatabaseModel(2, 'Segunda tarea test', 'in-progress')
    # TaskDatabaseOperations.add(newTask2.id, newTask2.description, newTask2.status)
    # newTask3 = TaskDatabaseModel(3, 'Tercera tarea test', 'in-progress')
    # TaskDatabaseOperations.add(newTask3.id, newTask3.description, newTask3.status)

    # print("Esta es la tarea a eliminar:", TaskDatabaseOperations.delete('2'))

    # for task in TaskDatabaseOperations.list():
    #    print(task)

    # print("Tarea que se va a actualizar:",TaskDatabaseOperations.update('3', 'Esta es una descripcion mas larga de la tercera tarea'))
    
    # for task in TaskDatabaseOperations.list():
    #    print(task)

if __name__ == '__main__':
    main()