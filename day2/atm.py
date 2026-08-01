balance = float(input("Enter your current balance: "))
choice = input("Do you want to withdraw or deposit? (w/d): ")

if choice == "w":
    withdrawal_amount = float(input("Enter the amount to withdraw (must be > 0): "))
    if withdrawal_amount <= 0:
        print("Invalid withdrawal amount. Please enter a positive value.")
    else:
        # Check if withdrawal violates the 1000 minimum balance rule
        if withdrawal_amount > (balance - 1000):
            print("Insufficient funds. You must maintain a minimum balance of 1000.")
        else:
            balance = balance - withdrawal_amount
            print("Transaction successful. Your current balance is:", balance)

elif choice == "d":
    deposit_amount = float(input("Enter the amount to deposit (must be multiple of 500): "))
    if deposit_amount <= 0 or deposit_amount % 500 != 0:
        print("Invalid deposit amount. Please enter a value that is a multiple of 500.")
    else:
        balance = balance + deposit_amount
        print("Transaction successful. Your current balance is:", balance)

else:
    print("Invalid choice. Please enter 'w' for withdraw or 'd' for deposit.")