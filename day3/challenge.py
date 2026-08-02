dob = input("Enter your date of birth (dd/mm/yyyy): ")
age = 2026 - int(dob.split('/')[-1])
print("Your age is:", age)