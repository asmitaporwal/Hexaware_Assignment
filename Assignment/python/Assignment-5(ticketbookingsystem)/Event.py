import mysql.connector as connection

from DBconnection import DbConn

class Event(DbConn):
    def __init__(self,event_id=None, event_name=None, event_date=None, event_time=None, venue_id=None, total_seats=None, available_seats=None, ticket_price=None, event_type=None, booking_id=None):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
        self.booking_id=booking_id

    def get_event_id(self):
        return self.event_id
    
    def set_event_id(self, event_id):
        self.event_id = event_id
    
    def get_event_name(self):
        return self.event_name
    
    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_date(self):
        return self.event_date
    
    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_time(self):
        return self.event_time
    
    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_venue_id(self):
        return self.venue_id
    
    def set_venue_id(self, venue_id):
        self.venue_id = venue_id

    def get_total_seats(self):
        return self.total_seats
    
    def set_total_seats(self, total_seats):
        self.total_seats = total_seats

    def get_available_seats(self):
        return self.available_seats
    
    def set_available_seats(self, available_seats):
        self.available_seats = available_seats

    def get_ticket_price(self):
        return self.ticket_price
    
    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_event_type(self):
        return self.event_type
    
    def set_event_type(self, event_type):
        self.event_type = event_type

    def calculate_total_revenue(self):
        try:
            self.open()
            self.c.execute(f"Select ticket_price*(total_seats - available_seats) From Event Where event_id = {self.event_id}")
            rev = self.c.fetchone()[0]
        except Exception as e:
            print(e)
        finally:
            self.close()
            return rev

    def get_booked_no_of_tickets(self):
        try:
            self.open()
            self.c.execute(f"Select (total_seats - available_seats) From Event Where event_id = {self.event_id}")
            num = self.c.fetchone()[0]
        except Exception as e:
            print(e)
        finally:
            self.close()
            return num

    def book_tickets(self, num_tickets):
        try:
            if num_tickets <= self.available_seats:
                self.open()
                self.c.execute(f"Update Event Set available_seats = ({self.available_seats} - {num_tickets}) Where event_id = {self.event_id}")
                self.mydb.commit()
                self.close()
                return True
            else:
                print(f"\nSorry.... we have only '{self.available_seats}' tickets available for the event '{self.event_name}'.")
                return False
        except Exception as e:
            print(e)

    def cancel_booking(self, num_tickets):
        try:
            self.open()
            self.c.execute(f"Update Event Set available_seats = ({self.available_seats} + {num_tickets}) Where event_id = {self.event_id}")
            self.mydb.commit()
            self.close()
        except Exception as e:
            print(e)

    def display_event_details(self):
        print("Event ID : ",self.event_id)
        print("Event Name : ",self.event_name)
        print("Event Date : ",self.event_date)
        print("Event Time : ",self.event_time)
        print("Venue ID : ",self.venue_id)
        print("Total Seats : ",self.total_seats)
        print("Available Seats : ",self.available_seats)
        print("Ticket Price : ",self.ticket_price)
        print("Event Type : ",self.event_type)