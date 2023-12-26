from Account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  

    def __init__(self, account_id=None, customer_id=None, account_type=None, account_balance=0.0,OVERDRAFT_LIMIT=0.0):
        super().__init__(account_id, customer_id, "Current", account_balance)
        self.OVERDRAFT_LIMIT=OVERDRAFT_LIMIT

    def withdraw(self, amount):
        if amount > self.get_account_balance() + self.OVERDRAFT_LIMIT:
            print("Withdrawal exceeds available funds and overdraft limit.")
        else:
            updated_balance = self.get_account_balance() - amount
            self.set_account_balance(updated_balance)
            print(f"Withdrew ${amount:.2f} successfully. Updated balance: ${updated_balance:.2f}")

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