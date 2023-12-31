class Order:
    def __init__(self, order_id, customer_id, order_date, total_price, shipping_address):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_price = total_price
        self.shipping_address = shipping_address