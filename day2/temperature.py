temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("It's freezing cold!")
elif 0 <= temperature < 10:
    print("It's very cold.")
elif 10 <= temperature < 20:
    print("It's cold.")
elif 20 <= temperature < 30:
    print("It's warm.")
elif 30 <= temperature < 40:
    print("It's hot.")
else:
    print("It's extremely hot!")