class CustomerNotFoundException(Exception):
    def __init__(self, message="CustomerNotFoundException"):
        self.message = message
        super().__init__(self.message)

class ProductNotFoundException(Exception):
    def __init__(self, message="ProductNotFoundException"):
        self.message = message
        super().__init__(self.message)

class OrderNotFoundException(Exception):
    def __init__(self, message="OrderNotFoundException"):
        self.message = message
        super().__init__(self.message)