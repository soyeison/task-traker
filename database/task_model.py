from datetime import datetime

class TaskDatabaseModel:
    def __init__(self, id, description, status, createdAt, updatedAt):
            self.id = id
            self.description = description
            self.status = status
            self.createdAt = createdAt
            self.updatedAt = updatedAt

    def __str__(self):
          return f"Tarea: {self.description} - status: {self.status} - ID: {self.id}"