class ArgumentNumberException(Exception):
    def __init__(self, message="Number of arguments is invalid"):
        self.message = message
        super().__init__(self.message)