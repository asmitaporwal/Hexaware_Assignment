from Booking import Booking


class MainEventManagement:
    def main():
        b=Booking()
        while True:
            print("\n---------- Event Management System Menu ----------")
            print("1. View Event Details")
            print("2. Calculate Total Revenue")
            print("3. Get Booked Number of Tickets")
            print("4. Book Tickets")
            print("5. Cancel Booking")
            print("6. Get Event Details")
            print("7. venue details")
            print("8. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please enter a valid option.")
                continue

            if choice == 1:
                event_id = int(input("Enter Event ID: "))
                event_details = b.get_event_details(event_id)
                print(event_details)

            elif choice == 2:
                event_id = int(input("Enter Event ID: "))
                revenue = b.calculate_total_revenue(event_id)
                print(f"Total Revenue for Event {event_id}: ${revenue}")

            elif choice == 3:
                event_id = int(input("Enter Event ID: "))
                booked_tickets = b.getBookedNoOfTickets(event_id)
                print(f"Booked Tickets for Event {event_id}: {booked_tickets}")

            elif choice == 4:
                event_id = int(input("Enter Event ID: "))
                num_tickets = int(input("Enter Number of Tickets to Book: "))
                customer_id = int(input("Enter Customer ID: "))
                total_cost = float(input("Enter Total Cost: "))
                booked = b.book_tickets(event_id, num_tickets, customer_id, total_cost)
                if booked:
                    print("Tickets booked successfully.")
                else:
                    print("Failed to book tickets.")

            elif choice == 5:
                booking_id = int(input("Enter Booking ID to cancel: "))
                customer_id=int(input("Enter customer Id: "))
                event_id = int(input("Enter Event ID: "))
                num_tickets = int(input("Enter Number of Tickets to Cancel: "))
                cancelled = b.cancel_booking(booking_id,customer_id, event_id, num_tickets)
                if cancelled:
                    print("Booking cancelled successfully.")
                else:
                    print("Failed to cancel booking.")

            elif choice == 6:
                id=int(input("Enter Event id: "))
                b.get_event_details(id)
            elif choice == 7:
                id=int(input("Enter Venue id: "))
                b.display_venue_details(id)
          
            elif choice == 8:
                print("\nThank You\n")
                break
            else:
                print("\nInvalid Choice!!\nPlease Try Again...\n")

if __name__ == "__main__":
    MainEventManagement.main()
