import csv

def calculate_next_id():
    try:
        with open('database.csv', 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            # El ultimo elemento guardado
            listReader = list(reader)
            lastItemOfList = listReader[len(listReader) - 1]
            nextId = int(lastItemOfList[0]) + 1
            return str(nextId)
    except:
        print("Something happend handling next id")
