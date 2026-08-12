# Royal Bank of Zambia (RBZ) - Python Script for Banking Operations

account = {"Name": "Mr. Jhon", "F/Name": "Mr. Jhon sr.", "Account no": "1234567", "Balance": 30000, "Status": "Active"}
service = ["1. Account", "2. Check Balance", "3. Deposit", "4. Withdraw", "5. Exit"]
print("Welcome to Royal Bank of Zambia(RBZ)")
for svc in service:
    print(svc)

while True:
    choice = input("Please select your services(1 to 5): ")

    if choice == "1":
        print("Account Details")
        for key, value in account.items():
            print(f"{key}: {value}")

    elif choice == "2":
        print("Your current balance is:", account["Balance"])

    elif choice == "3":
        try:
            deposit_amount = float(input("Enter your deposit amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
        else:
            if deposit_amount > 0:
                account["Balance"] += deposit_amount
                print("Deposit successful. Your new balance is:", account["Balance"])
            else:
                print("Deposit amount must be greater than 0.")

    elif choice == "4":
        try:
            withdraw_amount = float(input("Enter your withdrawal amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
        else:
            # Ensure a minimum balance of 999 remains after withdrawal
            if withdraw_amount > 0 and account["Balance"] - withdraw_amount >= 1000:
                account["Balance"] -= withdraw_amount
                print("Withdraw successful. Your new balance is:", account["Balance"])
            else:
                print("Withdrawal failed. Ensure amount is positive and leaves at least 1000 in the account.")

    elif choice == "5":
        print("Thank for being with us")
        break

    else:
        print("Please select right service")