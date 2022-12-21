class Error(Exception):
    """
    An unspecified error.

    """


class MissingPermission(Error):
    """
    Missing permission when calling the API.

    """
    
class InvalidData(Error):
    """
    Missing Data required for request

    Args:
        Error (_type_): _description_
    """

class AccountNotFound(Error):
    """
    Account not found

    Args:
        Error (_type_): _description_
    """
    
class ContactNotFound(Error):
    """
    Account not found

    Args:
        Error (_type_): _description_
    """
    
class TooManyAttempts(Error):
    """
    Too Many attempts to API

    Args:
        Error (_type_): _description_
    """