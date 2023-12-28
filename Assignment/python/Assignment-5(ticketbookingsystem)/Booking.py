from DBConnection import DBConnection
from datetime import datetime

class Booking(DBConnection):
    def get_event_details(self, event_id):
        try:
          self.open()
          query = f"SELECT * FROM event WHERE event_id = {event_id}"
          self.c.execute(query)
          event_data = self.c.fetchone()

          if event_data:
             print(f"Event ID: {event_data[0]}, Event Name: {event_data[1]}, Date: {event_data[2]}, Time: {event_data[3]}, Venue ID: {event_data[4]}, Available Seats: {event_data[5]}, Ticket Price: {event_data[6]}, Event Type: {event_data[7]}")
          else:
            print("Event not found.")

        except Exception as e:
          print("Error fetching event details:", e)
          return None

        finally:
         self.close()
    
    def display_venue_details(self, venue_id):
        try:
            self.open()
            query = f"SELECT * FROM venu WHERE venue_id = {venue_id}"
            self.c.execute(query)
            venue_data = self.c.fetchone()

            if venue_data:
                venue_id, venue_name, address = venue_data
                print(f"Venue ID: {venue_id}, Venue Name: {venue_name}, Address: {address}")
            else:
                print("Venue not found.")

        except Exception as e:
            print("Error fetching venue details:", e)

        finally:
            self.close()
       

    def calculate_total_revenue(self,event_id):
        try:
            self.open()
            query = f"SELECT SUM(total_cost) FROM booking WHERE event_id = {event_id}"
            self.c.execute(query)
            result = self.c.fetchone()
            if result:
                return result[0]
            else:
               return 0  
        except Exception as e:
            print("Error calculating total revenue:", e)
            return None
        finally:
            self.close()

    def getBookedNoOfTickets(self,event_id):
        try:
          self.open()
          query = f"SELECT SUM(num_tickets) FROM booking WHERE event_id = {event_id}"
          self.c.execute(query)
          result = self.c.fetchone()
          if result:
            return result[0]
          else:
            return 0  # If no bookings found for the event
        except Exception as e:
           print("Error retrieving booked tickets:", e)
           return None
        finally:
          self.close()

    def book_tickets(self,event_id, num_tickets, customer_id, total_cost):
        try:
          self.open()
          query = f"SELECT available_seats FROM event WHERE event_id = {event_id}"
          self.c.execute(query)
          available_seats = self.c.fetchone()[0]

          if available_seats >= num_tickets:
            updated_seats = available_seats - num_tickets
            update_query = f"UPDATE event SET available_seats = {updated_seats} WHERE event_id = {event_id}"
            self.c.execute(update_query)
            booking_date = datetime.now().date()
            booking_id=int(input("\nEnter booking id: "))
            insert_query = f"INSERT INTO booking (booking_id,customer_id, event_id, num_tickets, total_cost, booking_date) VALUES ({booking_id},{customer_id}, {event_id}, {num_tickets}, {total_cost}, '{booking_date}')"
            self.c.execute(insert_query)
            
            self.mydb.commit()
            return True
          else:
            print("Not enough available seats.")
            return False
        except Exception as e:
          print("Error booking tickets:", e)
          return False
        finally:
           self.close()      

    def cancel_booking(self, booking_id,customer_id, event_id, num_tickets):
        try:
          self.open()

          booking_query = f"SELECT * FROM booking WHERE booking_id = {booking_id}"
          self.c.execute(booking_query)
          booking_data = self.c.fetchone()

          if booking_data:
            booked_tickets = booking_data[3]
            query = f"SELECT available_seats FROM event WHERE event_id = {event_id}"
            self.c.execute(query)
            available_seats = self.c.fetchone()[0]

            query_total_seats = f"SELECT total_seats FROM event WHERE event_id = {event_id}"
            self.c.execute(query_total_seats)
            total_seats = self.c.fetchone()[0]

            updated_seats = available_seats + num_tickets

            if updated_seats <= total_seats:
                update_query = f"UPDATE event SET available_seats = {updated_seats} WHERE event_id = {event_id}"
                self.c.execute(update_query)

                delete_query = f"DELETE FROM booking WHERE booking_id = {booking_id} and customer_id={customer_id}"
                self.c.execute(delete_query)

                self.mydb.commit()
                return True
            else:
                print("Invalid number of tickets to cancel.")
                return False
          else:
            print("Booking not found.")
            return False

        except Exception as e:
          print("Error canceling booking:", e)
          return False
        finally:
          self.close()              

