class InternetException(Exception):
    """Raise when the User's computer is not connected with internet"""

    def __init__(self, reason):
        self.reason = reason
        super().__init__(self.reason)
        
    def __repr__(self):
        return f"Alice => {self.reason}"
