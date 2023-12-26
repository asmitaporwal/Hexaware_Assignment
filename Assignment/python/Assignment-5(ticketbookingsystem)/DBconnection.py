from DBproperty import PropUtil

import mysql.connector as connection

class DbConn():
    def __init__(self):
        pass

    def open(self):
        try:
            li = PropUtil.getPropertyString()
            self.mydb = connection.connect(host=li[0], username=li[1], password=li[2], database=li[3])
            self.c = self.mydb.cursor(buffered = True)
        except Exception as e:
            print(e)
    
    def close(self):
        self.c.close()