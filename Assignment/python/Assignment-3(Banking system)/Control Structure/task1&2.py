

class Main():
    def main():
         def check_balance(balance):
              print(f"Your current balance is: {balance}")
              pass
         def withdraw(balance):
             amount = int(input("Enter the amount to withdraw: "))
             if amount > balance:
               print("Insufficient funds")
             elif amount % 100 != 0 or amount % 500 != 0:
                print("Withdrawal amount must be in multiples of 100 or 500")
             else:
               balance -= amount
               print(f"Withdrawal successful. Remaining balance: {balance}")
               return balance



         def deposit(balance):
               amount = int(input("Enter the amount to deposit: "))
               balance += amount
               print(f"Deposit successful. Current balance: {balance}")
               return balance

         def atm_transaction():
                balance = float(input("Enter your current balance: "))
                return balance
         while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 Check if you are eligible for loan")
            print("\nPress-2. Check Balance")
            print("\nPress-3. Withdraw")
            print("\nPress-4. Deposit")
            print("\nPress-5 Exit")
            i=int(input())
            if i==1:
                credit_score=int(input("\nEnter your credit score: "))
                annual_income=int(input("\nEnter your annual income: "))
                if credit_score > 700 and annual_income >= 50000:
                    print("Congratulations! You are eligible for a loan.")
                else:
                    print("Sorry, you are not eligible for a loan based on the criteria.")
            elif i == 2:
                balance=atm_transaction()
                check_balance(balance)
            
            elif i == 3:
                balance=atm_transaction()
                balance = withdraw(balance)
            elif i == 4:
                balance=atm_transaction()
                balance = deposit(balance)
            elif i == 5:
                print("\nThank You\n")
                break 
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n') 

if __name__ == "__main__":
    Main.main()                  
    

       