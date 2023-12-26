from Event import Event

from DBconnection import DbConn

class Booking(DbConn):
    def __init__(self,booking_id, customer_id, event_id, num_tickets,total_cost,booking_date):
        self.booking_id=booking_id
        self.customer_id = customer_id
        self.event_id = event_id
        self.num_tickets = num_tickets
        self.total_cost=total_cost
        self.boking_date=booking_date
    
    def calculate_booking_cost(self):
        try:
            self.open()
            self.c.execute("Select * From Event Where event_id = {self.event_id}")
            eve = self.c.fetchone()
            self.close()
            return self.num_tickets * Event(*eve).get_ticket_price()
        except Exception as e:
            print(e)

    def book_tickets(self):
        try:
            self.open()
            self.c.execute(f"Select * From Event Where event_id = {self.event_id}")
            eve = self.c.fetchone()
            self.close()
            if Event(*eve).book_tickets(self.num_tickets):
                tc = self.num_tickets * Event(*eve).get_ticket_price()
                from datetime import timedelta, date
                bd = eve[2] - timedelta(days=4)
                self.open()
                self.c.execute(f"Insert Into Booking (booking_id,customer_id, event_id, num_tickets, total_cost, booking_date) Values ({self.booking_id},{self.customer_id}, {self.event_id}, {self.num_tickets}, {tc}, '{bd}') ")
                self.mydb.commit()
                bi = self.c.lastrowid
                self.close()
                print(f"\nBooking Done Successfully...\nYour Booking ID is : {bi}\nAmount to be Paid : {tc}")
                return bi
        except Exception as e:
            print(e)

    def cancel_booking(self):
        try:
            self.open()
            self.c.execute(f"Select * From Event Where event_id = {self.event_id}")
            eve = self.c.fetchone()
            self.close()
            Event(*eve).cancel_booking()
            tc = self.num_tickets * Event(*eve).get_ticket_price()
            self.open()
            self.c.execute(f"Delete From Bookig Where booking_id = {self.booking_id}")
            self.mydb.commit()
            self.close()
            print(f"\nCancellation successful... \nRefund amount: {tc}")
            return self.booking_id
        except Exception as e:
            print(e)

    def get_available_no_of_tickets(self):
        try:
            self.open()
            self.c.execute(f"Select * From Event Where event_id = {self.event_id}")
            eve = self.c.fetchone()
            self.close()
            return Event(*eve).available_seats
        except Exception as e:
            print(e)

    def get_event_details(self):
        try:
            self.open()
            self.c.execute(f"Select * From Event Where event_id = {self.event_id}")
            eve = self.c.fetchone()
            self.close()
            Event(*eve).display_event_details()
        except Exception as e:
            print(e)