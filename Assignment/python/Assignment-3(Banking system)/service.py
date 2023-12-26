from DBconnection import DBConnection

class serviceprovider(DBConnection):
    def get_account_balance(self, account_number):
        try:
            self.open()
            query = f"SELECT balance FROM accounts WHERE account_id = {account_number}"
            self.c.execute(query)
            result = self.c.fetchone()
            if result:
                return result[0]
            else:
                print("Account not found")
        except Exception as e:
            print("Error occurred while retrieving account balance:", e)
            return None  
        finally:
            self.close()

    def transfer(self, id,from_account_number, to_account_number, amount):
        try:
            self.open()

            
            query = f"UPDATE accounts SET balance = balance - {amount} WHERE account_id = {from_account_number}"
            self.c.execute(query)
            self.mydb.commit()

            
            query = f"UPDATE accounts SET balance = balance + {amount} WHERE account_id = {to_account_number}"
            self.c.execute(query)
            self.mydb.commit()

           
            query = f"INSERT INTO transactions (transaction_id,account_id, transaction_type, amount) VALUES ({id},{from_account_number}, 'Debit', {amount})"
            self.c.execute(query)
            self.mydb.commit()

            query = f"INSERT INTO transactions (transaction_id,account_id, transaction_type, amount) VALUES ({id+1},{to_account_number}, 'Credit', {amount})"
            self.c.execute(query)
            self.mydb.commit()

            print("Transfer successful.")
        except Exception as e:
            print("Error occurred during transfer:", e)
        finally:
            self.close()        
    