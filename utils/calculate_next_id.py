import csv
import config

def calculate_next_id():
    try:
        with open(config.DATABASE_FILE, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            # El ultimo elemento guardado
            listReader = list(reader)
            if len(listReader) == 0:
                return '1'
            lastItemOfList = listReader[len(listReader) - 1]
            nextId = int(lastItemOfList[0]) + 1
            return str(nextId)
    except:
        print("Something happend handling next id")
