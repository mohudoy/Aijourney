month = int(input("Enter the month (1-12): "))
temp = int(input("Enter the temperature in Celsius: "))
if month == 1 and temp <= 20:
    print("January, its winter season")
elif month == 2 and temp <= 20:
    print("February, its winter season")
elif month == 3 and temp >= 20 and temp <= 50:
    print("March, its summer season")
elif month == 4 and temp >= 20 and temp <= 50:
    print("April, its summer season")
elif month == 5 and temp >= 20 and temp <= 50:
    print("May, its summer season")
elif month == 6 and temp >= 20 and temp <= 50:
    print("June, its summer season")
elif month == 7 and temp >= 10 and temp <= 40:
    print("July, its rainy season")
elif month == 8 and temp >= 10 and temp <= 40:
    print("August, its rainy season")
elif month == 9 and temp >= 10 and temp <= 40:
    print("September, its rainy season")
elif month == 10 and temp >= 10 and temp <= 40:
    print("October, its rainy season")
elif month == 11 and temp <= 20:
    print("November, its winter season")
elif month == 12 and temp <= 20:
    print("December, its winter season")
else:
    print("Invalid month or temperature or something unusual.")