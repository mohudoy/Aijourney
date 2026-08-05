first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
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
        print(round(first_number / second_number, 2))
else:
    print("you need to choose an operation from (+, -, *, /) only.")