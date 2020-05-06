
# See https://docs.python.org/3/tutorial/errors.html#raising-exceptions
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidActionError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, action, board, message):
        print('InvalidActionError: ', message, 'Action: ', action, 'on board: ', board)
