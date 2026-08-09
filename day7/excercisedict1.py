cricketer = {"Name": "Shakib Al Hasan", "Age": 35, "Country": "Bangladesh", "Batting Style": "Left-hand bat", "Bowling Style": "Left-arm orthodox spin", "Role": "All-rounder", "Matches Played": 200, "Runs Scored": 6000, "Wickets Taken": 250, "Highest Score": 200, "Best Bowling Figures": "6/30"}
for key, value in cricketer.items():
    print(f"{key}: {value}")

check = input("Enter a key to check: ") .title()
if check in cricketer:
    print(f"{check}: {cricketer[check]}")
else:
    print("Key not found.")

add_key = input("Enter a key to add: ") .title()
add_value = input("Enter a value for the key: ") .title()
cricketer[add_key] = add_value
print("Cricketer new dictionary: ")
for key, value in cricketer.items():
    print(f"{key}: {value}")

update = input("Enter a field to update: ") .title()
if update in cricketer:
    new_value = input(f"Enter the new value for {update}: ") .title()
    cricketer[update] = new_value
    print("Cricketer dictionary after updating the field:")
    for key, value in cricketer.items():
        print(f"{key}: {value}")
else:
    print("Field not found.")