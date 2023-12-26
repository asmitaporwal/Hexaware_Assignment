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