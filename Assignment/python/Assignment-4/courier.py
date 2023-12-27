from DBconnection import DBConnection
class Courier(DBConnection):
    def __init__(self, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber, deliveryDate, userId):
        self.courierID = courierID
        self.senderName = senderName
        self.senderAddress = senderAddress
        self.receiverName = receiverName
        self.receiverAddress = receiverAddress
        self.weight = weight
        self.status = status
        self.trackingNumber = trackingNumber
        self.deliveryDate = deliveryDate
        self.userId = userId

    # Getters for Courier attributes
    def get_courier_id(self):
        return self.courierID

    def get_sender_name(self):
        return self.senderName

    def get_sender_address(self):
        return self.senderAddress

    def get_receiver_name(self):
        return self.receiverName

    def get_receiver_address(self):
        return self.receiverAddress

    def get_weight(self):
        return self.weight

    def get_status(self):
        return self.status

    def get_tracking_number(self):
        return self.trackingNumber

    def get_delivery_date(self):
        return self.deliveryDate

    def get_user_id(self):
        return self.userId

    # Setters for Courier attributes
    def set_courier_id(self, courierID):
        self.courierID = courierID

    def set_sender_name(self, senderName):
        self.senderName = senderName

    def set_sender_address(self, senderAddress):
        self.senderAddress = senderAddress

    def set_receiver_name(self, receiverName):
        self.receiverName = receiverName

    def set_receiver_address(self, receiverAddress):
        self.receiverAddress = receiverAddress

    def set_weight(self, weight):
        self.weight = weight

    def set_status(self, status):
        self.status = status

    def set_tracking_number(self, trackingNumber):
        self.trackingNumber = trackingNumber

    def set_delivery_date(self, deliveryDate):
        self.deliveryDate = deliveryDate

    def set_user_id(self, userId):
        self.userId = userId

    def place_order(self):
        try:
            self.open()

            query = f"INSERT INTO courier (CourierId, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, UserId) VALUES ({self.courierID}, '{self.senderName}', '{self.senderAddress}', '{self.receiverName}', '{self.receiverAddress}', {self.weight}, '{self.status}', {self.trackingNumber}, '{self.deliveryDate}', {self.userId})"
            self.c.execute(query)
            self.mydb.commit()

            print("Courier order placed successfully.")
            return self.trackingNumber
        except Exception as e:
            print("Error occurred while placing order:", e)
            return None
        finally:
            self.close()
    