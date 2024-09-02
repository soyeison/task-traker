class ValidateIdException(Exception):
    def __init__(self, message = "The id entered is invalid"):
        self.message = message
        super().__init__(message)