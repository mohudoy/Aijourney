age = input("What is your age?")
gender = input("What is your gender? (M/F)").upper()
if gender == "M":
    if int(age) >= 21:
        print("You are a man and You are eligible to marry.")
    else:
        print("You are a man and You are not eligible to marry.")
elif gender == "F":
    if int(age) >= 19:
        print("You are a woman and  you are eligible to marry.")
    else:
        print("You are a woman and you are not eligible to marry.")
else:
    print("Invalid gender. Please enter M or F.")