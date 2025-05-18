class RankException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid rank exception."
        super().__init__(message)

class SuitException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid suit exception."
        super().__init__(message)

class InvalidArgumentException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid argument provided."
        super().__init__(message)