import argparse
from domain.task_domain import TaskDomain
from utils.validate_list_option import validate_list_option
from utils.validate_id import validate_id
from errors.argument_number_exception import ArgumentNumberException
from errors.write_csv_file_exception import WriteCsvFileException
from errors.dont_exist_task_id import DontExistTaskId
from errors.validate_id_exception import ValidateIdException

def main():
    parser = argparse.ArgumentParser(description="Manage your tasks CLI")

    parser.add_argument('operation', choices=['add', 'list', 'update', 'delete', 'mark-in-progress', 'mark-done'], help="Available operations")
    parser.add_argument('data', type=str, nargs='*')

    args = parser.parse_args()

    try:
        # Validar que si se proporcionan los argumentos que son. En este caso, la variable data debe contener solo 1 elemento
        if args.operation == 'add':
            # Sino lanzar error
            if len(args.data) != 1:
                raise ArgumentNumberException()
            newTask = TaskDomain.add(args.data[0])
            print(f"Task added successfully (ID: {newTask})")

        elif args.operation == 'list':
            if len(args.data) == 0:
                for task in TaskDomain.list():
                    print(task)
            elif len(args.data) == 1:
                if validate_list_option(args.data[0]) == False:
                    raise ArgumentNumberException() # Modificar esta excepcion para agregar una particular que hable sobre opciones
                else:
                    for task in TaskDomain.list(args.data[0]):
                        print(task)
            elif len(args.data) > 1:
                raise ArgumentNumberException()
            
        elif args.operation == 'delete':
            print(TaskDomain.delete(args.data[0]))
        
        elif args.operation == 'update':
            if len(args.data) == 0 or len(args.data) > 2:
                raise ArgumentNumberException()
            
            if validate_id(args.data[0]) == False:
                raise ValidateIdException(f"The id: {args.data[0]} is invalid")

            print(TaskDomain.update(args.data[0], args.data[1]))
        
        elif args.operation == 'mark-in-progress':
            if len(args.data) == 0 or len(args.data) > 1:
                raise ArgumentNumberException()
            
            if validate_id(args.data[0]) == False:
                raise ValidateIdException(f"The id: {args.data[0]} is invalid")

            print(TaskDomain.markProgress(args.data[0], 'mark-in-progress'))

        elif args.operation == 'mark-done':
            if len(args.data) == 0 or len(args.data) > 1:
                raise ArgumentNumberException()
            
            if validate_id(args.data[0]) == False:
                raise ValidateIdException(f"The id: {args.data[0]} is invalid")
            
            print(TaskDomain.markProgress(args.data[0], 'mark-done'))

    except ArgumentNumberException as e:
        print(f"Error: {e}")
    except WriteCsvFileException as e:
        print(f"Error: {e}")
    except DontExistTaskId as e:
        print(f"Error: {e}")
    except ValidateIdException as e:
        print(f"Error: {e}")
    except:
        print("Contact to support")


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