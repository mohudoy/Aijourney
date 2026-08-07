
try:
    first_number = float(input("Enter the first number: "))
except ValueError:
    print("You need to enter number only.")
    raise SystemExit

try:
    second_number = float(input("Enter the second number: "))
except ValueError:
    print("You need to enter a number only.")
    raise SystemExit

choose_operation = input("Choose an operation (+, -, *, /): ")

if choose_operation in ("+", "-", "*", "/"):
    print("The result is: ", end=" ")

    if choose_operation == "+":
        print(first_number + second_number)
    elif choose_operation == "-":
        print(first_number - second_number)
    elif choose_operation == "*":
        print(first_number * second_number)
    elif choose_operation == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            print(round(first_number / second_number, 2))
else:
    print("You need to choose an operation from (+, -, *, /) only.")