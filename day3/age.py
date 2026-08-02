dob = input("Enter your date of birth (dd/mm/yyyy): ")
age = 2026 - int(dob.split('/')[-1])
print("Your age is:", age)
if age < 18:
    print("You are a minor.")
elif age >= 60:
    print("You are a senior citizen.")
elif age >= 33:
    print("You are not eligible for govt. jobs.")
elif age >= 25:
    print("You are eligible to participate in the member of parliament election.")
else:
    print("You are a voter")