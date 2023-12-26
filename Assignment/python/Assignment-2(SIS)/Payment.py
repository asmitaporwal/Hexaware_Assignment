from DBconnection import DBConnection
class Payment(DBConnection):
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date

    def MakePayment(self):
        try:
            self.open()
            self.c.execute(f" INSERT INTO Payments (payment_id,student_id, amount, payment_date) VALUES ('{self.payment_id}','{self.student_id}', '{self.amount}', '{self.payment_date}')")
            self.mydb.commit()
            print("Recorded payment successfully.")
        except Exception as e:
            print("Error while recording payment:", e)
        finally:
            self.close()    