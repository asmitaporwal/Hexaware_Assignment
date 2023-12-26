def display_transactions(transactions):
    print("Transaction History:")
    for index, transaction in enumerate(transactions, start=1):
        print(f"{index}. {transaction}")

def main():
    transactions = []

    while True:
        print("\nOptions:")
        print("1. Add Deposit")
        print("2. Add Withdrawal")
        print("3. Display Transaction History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            deposit = float(input("Enter deposit amount: "))
            transactions.append(f"Deposit: +{deposit}")
            print("Deposit added successfully!")
        elif choice == '2':
            withdrawal = float(input("Enter withdrawal amount: "))
            transactions.append(f"Withdrawal: -{withdrawal}")
            print("Withdrawal added successfully!")
        elif choice == '3':
            display_transactions(transactions)
        elif choice == '4':
            display_transactions(transactions)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
