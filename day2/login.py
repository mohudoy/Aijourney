id = input("Enter your ID: ")
password = input("Enter your password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long. Please try again.")
    password = input("Enter your password: ")
confirm_password = input("Confirm your password: ")
if password == confirm_password:
    print("Your id is:", id)
else:
    print("Passwords do not match. Please try again.")
while id == input("Enter your ID: ") and password == input("Enter your password: "):
        print("Login successful!")
        break
else:
    print("Invalid ID or password. Please try again.")
