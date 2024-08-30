from datetime import datetime

class TaskDatabaseModel:
    def __init__(self, id, description, status):
            self.id = id
            self.description = description
            self.status = status
            self.createdAt = datetime.now()
            self.updatedAt = datetime.now()

    def __str__(self):
          return f"Tarea: {self.description}"