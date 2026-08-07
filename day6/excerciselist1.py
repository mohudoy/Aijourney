foods = ["Vat", "Macch", "Alu Vorta", "Dal", "Mishti", "Doi", "Pitha", "Chicken", "Beef", "Mutton"]
search = input("Enter a food name: ").title()
if search in foods:
    print(f"{search} is in the list.")
else:
    print("Please enter a valid food name from the list.")

for food in foods:
    print(food)

while True:
    quit = input("Do you want to quit? (Yes/No): ").title()
    if quit == "Yes":
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("You can continue using the program.")
        add_food = input("Enter a food name to add: ").title()
        if add_food not in foods:
            foods.append(add_food)
            print(f"{add_food} has been added to the list.")
        else:
            print(f"{add_food} is already in the list.")

        remove_food = input("Enter a food name to remove: ").title()
        if remove_food in foods:
            foods.remove(remove_food)
            print(f"{remove_food} has been removed from the list.")
        else:
            print(f"{remove_food} is not in the list.")

        new_list = foods.copy()
        for food in new_list:
            print(food)