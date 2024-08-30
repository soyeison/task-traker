class ReadCsvFileException(Exception):
    def __init__(self, message = "Error while read csv file"):
        self.message = message
        super().__init__(message)