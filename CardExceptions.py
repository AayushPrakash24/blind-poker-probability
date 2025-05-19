class InvalidArgumentException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid argument provided."
        super().__init__(message)

class InvalidHandException(Exception):
    def __init__(self, message=None):
        if not message:
            message = "Invalid hand exception."
        super().__init__(message)

class RankException(InvalidArgumentException):
    def __init__(self, message=None):
        if not message:
            message = "Invalid rank exception."
        super().__init__(message)

class SuitException(InvalidArgumentException):
    def __init__(self, message=None):
        if not message:
            message = "Invalid suit exception."
        super().__init__(message)

class IncompleteHandException(InvalidHandException):
    def __init__(self, message=None):
        if not message:
            message = "Incomplete hand exception."
        super().__init__(message)
