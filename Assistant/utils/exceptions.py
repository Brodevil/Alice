class InternetException(Exception):
    """Raise when the User's computer is not connected with internet"""

    def __init__(self, reason):
        self.reason = reason
        super().__init__(self.reason)
        
    def __repr__(self):
        return f"Alice => {self.reason}"


class EnvFileValueError(Exception):
    """ Raised when any problem regarding the env files, just like email had not return or password
    inside the env lots of data had been required """

    def __init__(self, error):
        self.error = error

    def __repr__(self):
        return f"Alice => {self.error}"
    
    