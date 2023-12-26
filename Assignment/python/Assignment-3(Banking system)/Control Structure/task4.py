
customer_accounts = {
    12345: 1500.00,
    67890: 2500.00,
    13579: 500.00
}


def check_balance(account_number):
    if account_number in customer_accounts:
        return customer_accounts[account_number]
    else:
        return None


while True:
    try:
        account_number = int(input("Enter your account number: "))
        balance = check_balance(account_number)
        
        if balance is not None:
            print(f"Your account balance is: ${balance:.2f}")
            break
        else:
            print("Invalid account number. Please try again.")
    except ValueError:
        print("Please enter a valid account number (numeric value).")
