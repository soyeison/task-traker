import argparse
from database.TaskDatabase import TaskDatabaseOperations
from database.TaskModel import TaskDatabaseModel
from classes.TaskDomain import TaskDomain
from errors.ArgumentNumberException import ArgumentNumberException
from errors.WriteCsvFileException import WriteCsvFileException

def main():
    parser = argparse.ArgumentParser(description="Manage your tasks CLI")

    parser.add_argument('operation', choices=['add', 'list', 'update', 'delete', 'mark-in-progress', 'mark-done'], help="Available operations")
    parser.add_argument('data', type=str, nargs='*')

    args = parser.parse_args()

    try:
        if args.operation == 'add':
            # Validar que si se proporcionan los argumentos que son
            # En este caso, la variable data debe contener solo 1 elemento
            # Sino lanzar error
            if len(args.data) != 1:
                raise ArgumentNumberException()
            newTask = TaskDomain(args.data[0])
            newTask.add()
        elif args.operation == 'list':
            if len(args.data) > 1:
                raise ArgumentNumberException()
            for task in TaskDomain.list():
                print(task)
    except ArgumentNumberException as e:
        print(f"Error: {e}")
    except WriteCsvFileException as e:
        print(f"Error: {e}")
    except:
        print("Otro tipo de error sucedio")


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