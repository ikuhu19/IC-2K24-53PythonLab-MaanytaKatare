def run_atm():
    balance = 5000
    pin = "1234"
    
    user_pin = input("Enter PIN to continue: ")
    if user_pin != pin:
        print("Incorrect PIN. Exiting.")
        return

    while True:
        print("\n1. Check Balance | 2. Deposit | 3. Withdraw | 4. Change PIN | 5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Current Balance: {balance}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            balance += amount
            print(f"Deposited successfully. New balance: {balance}")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount > balance:
                print("Error: Insufficient funds. Transaction rejected.")
            else:
                balance -= amount
                print(f"Please take your cash. New balance: {balance}")
        elif choice == '4':
            pin = input("Enter new PIN: ")
            print("PIN changed successfully.")
        elif choice == '5':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_atm()