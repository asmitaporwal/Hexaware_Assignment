from DBconnection import DBConnection
class Account(DBConnection):
    def __init__(self, account_id,customer_id=None, account_type=None, account_balance=0.0):
        self.account_id = account_id
        self.customer_id=customer_id
        self.account_type = account_type
        self.account_balance = account_balance

    def get_account_id(self):
        return self.account_id

    def set_account_number(self, account_id):
        self.account_id = account_id

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_balance(self):
        return self.account_balance

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def print_account_info(self):
        print(f"Account Number: {self.account_id}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: ${self.account_balance:.2f}")

    def account_exists(self, account_id):
        try:
            self.open()
            query = f"SELECT COUNT(*) FROM accounts WHERE account_id = {account_id}"
            self.c.execute(query)
            result = self.c.fetchone()
            return result[0] > 0
        except Exception as e:
            print("Error while checking account existence:", e)
            return False
        finally:
            self.close()

    def deposit(self, amount):
        try:
            self.open()
            current_balance = self.get_account_balance()
            updated_balance = current_balance + amount

            query = f"UPDATE accounts SET balance = {updated_balance} WHERE account_id = {self.account_id}"
            self.c.execute(query)
            self.mydb.commit()

            self.set_account_balance(updated_balance)
            print(f"Deposited ${amount:.2f} successfully. Updated balance: ${updated_balance:.2f}")
        except Exception as e:
            print("Error occurred during deposit:", e)
        finally:
            self.close()
        

    def withdraw(self, amount):
        try:
            self.open()
            current_balance = self.get_account_balance()

            if amount > current_balance:
                print("Insufficient balance. Withdrawal failed.")
            else:
                updated_balance = current_balance - amount
                query = f"UPDATE accounts SET balance = {updated_balance} WHERE account_id = {self.account_id}"
                self.c.execute(query)
                self.mydb.commit()

                self.set_account_balance(updated_balance)
                print(f"Withdrew ${amount:.2f} successfully. Updated balance: ${updated_balance:.2f}")
        except Exception as e:
            print("Error occurred during withdrawal:", e)
        finally:
            self.close()  

    def calculate_interest(self):
        try:
            self.open()
            current_balance = self.get_account_balance()

            interest_rate = 4.5

            interest_amount = (current_balance * interest_rate) / 100

            print(f"Interest Amount at {interest_rate}%: ${interest_amount:.2f}")
        except Exception as e:
            print("Error occurred while calculating interest:", e)
        finally:
            self.close()              