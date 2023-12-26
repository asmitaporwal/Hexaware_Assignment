class EventNotFoundException(Exception):
    def __init__(self, message="EventNotFoundException"):
        self.message = message
        super().__init__(self.message)

class InvalidBookingIDException(Exception):
    def __init__(self, message="InvalidBookingIDException"):
        self.message = message
        super().__init__(self.message)