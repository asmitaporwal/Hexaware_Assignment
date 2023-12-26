from Account import Account

class SavingsAccount(Account):
    def __init__(self, account_id=None, customer_id=None, account_type=None, account_balance=None, interest_rate=0.0):
        super().__init__(account_id, customer_id, "Saving", account_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.get_account_balance() * (self.interest_rate / 100)
        updated_balance = self.get_account_balance() + interest_amount
        self.set_account_balance(updated_balance)
        print(f"Interest calculated: ${interest_amount:.2f}. Updated balance: ${updated_balance:.2f}")

    def create_account_in_db(self):
        try:
            self.open()
            query = f"INSERT INTO accounts(account_id, customer_id, account_type, balance) VALUES ({self.account_id}, {self.customer_id}, '{self.account_type}', {self.account_balance})"
            self.c.execute(query)
            self.mydb.commit()
            print("Account details inserted into the database.")
        except Exception as e:
            print("Error occurred while inserting account details:", e)
        finally:
            self.close()    