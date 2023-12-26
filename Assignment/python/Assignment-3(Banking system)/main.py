from Account import Account
from SavingAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from service import serviceprovider
class Main():
    def main():
         s=serviceprovider()
         while True:
            print("\n----------Main Menu----------")
            print("\nPress-1 Deposit amount")
            print("Press-2 Withdraw amount")
            print("Press-3 Calculate interest")
            print("Press-4 Create Savings Account")
            print("Press-5 Create Current Account")
            print("Press-6 Check balance")
            print("Press-7 Transfer money")
            print("Press-8 Exit")
            i = int(input())
            
            if i == 1:
                aid = int(input("Enter account id: "))
                acc = Account(aid)
                if acc.account_exists(aid):
                    cid = int(input("Enter customer id: "))
                    type = input("Enter account type: ")
                    balance = int(input("Enter account balance: "))
                    deposit = int(input("Enter deposit amount: "))
                    Account(aid, cid, type, balance).deposit(deposit)
                else:
                    print("Account does not exist.")
            elif i == 2:
                aid = int(input("Enter account id: "))
                acc = Account(aid)
                if acc.account_exists(aid):
                    cid = int(input("Enter customer id: "))
                    type = input("Enter account type: ")
                    balance = int(input("Enter account balance: "))
                    withdraw_amount = int(input("Enter withdrawal amount: "))
                    Account(aid,cid,type,balance).withdraw(withdraw_amount)
                else:
                    print("Account does not exist.")
            elif i == 3:
                aid = int(input("Enter account id: "))
                acc = Account(aid)
                if acc.account_exists(aid):
                    cid = int(input("Enter customer id: "))
                    type = input("Enter account type: ")
                    balance = int(input("Enter account balance: "))
                    Account(aid,cid,type,balance).calculate_interest()
                else:
                    print("Account does not exist.")
            elif i == 4:
                aid = int(input("Enter account id: "))
                cid = int(input("Enter customer id: "))
                balance = int(input("Enter account balance: "))
                interest_rate = float(input("Enter interest rate: "))
                acc = SavingsAccount(aid, cid, "Savings", balance, interest_rate).create_account_in_db()
                print("Savings Account created successfully.")
            elif i == 5:
                aid = int(input("Enter account id: "))
                cid = int(input("Enter customer id: "))
                balance = int(input("Enter account balance: "))
                overdraft_limit = float(input("Enter overdraft limit: "))
                acc = CurrentAccount(aid, cid, "Current", balance, overdraft_limit).create_account_in_db()
                print("Current Account created successfully.")
            elif i == 6:
                acc_number = int(input("Enter account number to check balance: "))
                balance = s.get_account_balance(acc_number)
                if balance is not None:
                  print(f"Account balance: ${balance:.2f}")
                else:
                  print("Account not found or an error occurred.")  
            elif i == 7:
                tid=int(input("Enter transaction id: "))
                from_account = int(input("Enter sender's account number: "))
                to_account = int(input("Enter receiver's account number: "))
                amount = float(input("Enter amount to transfer: "))

                sender_account = Account(from_account)
                receiver_account = Account(to_account)

                if sender_account.account_exists(from_account) and receiver_account.account_exists(to_account):
                    sender_balance = s.get_account_balance(from_account)
                    if sender_balance >= amount:
                        s.transfer(tid, from_account, to_account, amount)
                    else:
                      print("Insufficient funds.")
                else:
                  print("One or both accounts not found.")
            elif i == 8:
                print("\nThank You\n")
                break
            else:
                print('\nInvalid Choice!!\nPlease Try Again...\n')

if __name__=="__main__":
    Main.main()

