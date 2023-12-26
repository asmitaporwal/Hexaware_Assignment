import mysql.connector as connection

from DBconnection import DbConn

from Event import Event

from Serviceprovider import TicketBookingSystem

from exceptions import EventNotFoundException, InvalidBookingIDException

class TicketBookingApp(DbConn):
    def __init__(self):
        pass

    def main(self):
        tbs = TicketBookingSystem()
        while True:
            print("\n\n------------------MAIN MENU-------------------")
            print("Press-1 to Host a New Event")
            print("Press-2 to Book Tickets for an Event")
            print("Press-3 to View an Existing Booking")
            print("Press-4 to Cancel a Booking")
            print("Press-5 to Exit")
            ch = int(input())
            if ch == 1:
                id=int(input("Enter event id: "))
                en = input('Enter the Event Name : ')
                dic = {'S':'Sports', 'C':'Concert', 'M':'Movie'}
                try:
                    et = dic[input("Select the Event Type .. \nPress 'S' for Sports, 'C' for Concert, and 'M' for Movies : ").upper()]
                except Exception as e:
                    print('We dont have Venue for any such Event Type.. \nRedirecting to Main Menu..')
                    continue
                d = input("Enter Date in the 'yyyy-mm-dd' format : ")
                t = input("Enter Time in the 'hh:mm:ss' format : ")
                self.open()
                self.c.execute(f"Select * From Event Where event_type = '{et}' And event_date <> '{d}' Order By Rand() Limit 1")
                ven = self.c.fetchone()
                self.close()
                try:
                    vid = ven[4]
                except Exception as e:
                    print('No Venues are Available for the entered Date...!!')
                    continue
                ttls = int(input('Enter the Total Seats for the Event : '))
                avls = int(input('Enter the Available Tickets for the Event : '))
                tp = float(input('What should be the ticket price : '))
                tbs.create_event(event_id=id,event_name=en, date=d, time=t, venue_id=vid, total_seats=ttls, available_seats=avls, ticket_price=tp, event_type=et)
            elif ch == 2:
                print("Press-1 to Display a Particular Event Details")
                print("Press-2 to Display Events of a Particular Type")
                p = int(input())
                if p == 1:
                    eid = input('Enter the Event id : ')
                    self.open()
                    self.c.execute(f"Select * From Event Where event_id = '{eid}' ")
                    eve = self.c.fetchone()
                    self.close()
                    try:
                        if eve == None or eve == []:
                            raise EventNotFoundException("EventNotFoundException : No Event Exists with such a Name(Try typing the exact Event Name).")
                    except Exception as e:
                        print(e)
                        continue
                    else:
                        ob = Event(*eve)
                        tbs.display_event_details(ob)
                elif p == 2:
                    print('Select the Event Type you are looking to attend...')
                    print("Press 'S' for Sports, 'C' for Concert, and 'M' for Movies")
                    d = {'S':'Sports', 'C':'Concert', 'M':'Movie'}
                    try:
                        et = d[input().upper()]
                    except Exception as e:
                        print('\nWe dont have Event Type.. \nPlease Select a Valid Event_Type..\nRedirecting to Main Menu..')
                        continue
                    self.open()
                    self.c.execute(f"Select * From Event Where event_type = '{et}' ")
                    arr = self.c.fetchall()
                    for i in arr:
                        Event(*i).display_event_details()
                        print('\n')
                    self.close()
                    eve = None
                    id = int(input('From the list above, enter the ID of Event you are intrested to attend : '))
                    for i in arr:
                        if i[0] == id:
                            eve = i
                    if eve == None:
                        print('No such Event ID exists in the above list!!')
                        continue
                    ob = Event(*eve)
                else:
                    print('Invalid Choice.. Redirecting to Main Menu...')
                    continue
                num = int(input('Enter the Number Of Tickets you want to Book : '))
                tbs.book_tickets(ob, num)
            elif ch == 3:
                bi = int(input("Enter Booking ID to retrieve Boooking Details : "))
                self.open()
                self.c.execute(f"Select * From Booking Where booking_id = {bi}")
                bd = self.c.fetchone()
                self.close()
                try:
                    if bd == None or bd == []:
                        raise InvalidBookingIDException('InvalidBookingIDException : No such Booking has been made..\nRedirecting to Main Menu...')
                except Exception as e:
                    print(e)
                    continue
                else:
                    print('Customer ID : ',bd[1])
                    print('Event ID : ',bd[2])
                    print('Number of Tickets Booked : ',bd[3])
                    print('Total Cost of Booking : ',bd[4])
                    print('Booking Date : ',bd[5])
            elif ch == 4:
                self.open()
                bi = int(input("Enter Booking ID to be Cancelled : "))
                self.c.execute(f"Select event_id From Booking Where booking_id = {bi}")
                ei = self.c.fetchone()
                self.close()
                try:
                    if ei == None or ei == []:
                        raise InvalidBookingIDException('InvalidBookingIDException : No such Booking has been made..\nRedirecting to Main Menu...')
                except Exception as e:
                    print(e)
                    continue
                eid = ei[0]
                self.open()
                self.c.execute(f"Select * From Event Where event_id = {eid}")
                eveob = Event(*(self.c.fetchone()))
                self.close()
                self.open()
                self.c.execute(f"Select num_tickets From Booking Where booking_id = {bi}")
                nt = self.c.fetchone()[0]
                self.close()
                tbs.cancel_tickets(eveob, nt)
                self.open()
                self.c.execute(f"Delete From Booking Where booking_id = {bi}")
                self.mydb.commit()
                self.close()
                print('Booking has been cancelled for the Bookin ID : ',bi)
            elif ch == 5:
                print('Thank You...\nPlease Visit Again.....\n')
                break
            else:
                print('\nInvalid Choice.. Please Try Again....')


if __name__ == '__main__':
    TicketBookingApp().main()