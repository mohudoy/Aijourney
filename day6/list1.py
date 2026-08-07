try:
    districts = ["Dhaka", "Kishoreganj", "Khulna", "Mongla", "Rajshahi", "Barishal", "Sylhet", "Rangpur", "Comilla", "Jessore", "Cox's Bazar", "Chittagong", "Narsingdi", "Tangail", "Pabna", "Bogra", "Dinajpur", "Mymensingh", "Feni", "Noakhali", "Brahmanbaria", "Natore", "Jamalpur", "Sirajganj", "Habiganj", "Kushtia", "Pirojpur", "Satkhira", "Bhola", "Meherpur", "Netrokona", "Sherpur", "Lalmonirhat", "Gaibandha", "Kurigram", "Thakurgaon", "Joypurhat", "Naogaon", "Chapai Nawabganj"]
    index = int(input("Enter a district number (0-38): "))
    if 0 <= index < len(districts):
        print(districts[index])
    else:
        print("Index out of range. Please enter a valid district number between 0 and 38")
except ValueError:
    print("Please enter a valid district number between 0 and 38")

remove_district = input("Enter a district name to remove: ") .title()
if remove_district in districts:
    districts.remove(remove_district)
    print(f"{remove_district} has been removed from the list.")
else:
    print(f"{remove_district} is not in the list.")

new_district = input("Enter a new district name to add: ") .title()
if new_district not in districts:
    districts.append(new_district)
    print(f"{new_district} has been added to the list.")
else:
    print(f"{new_district} is already in the list.")


for district in districts:
    print(district)

input_district = input("Enter a district name to check if it exists in the list: ") .title()
if input_district in districts:
    print(f"{input_district} exists in the list.")
else:
    print(f"{input_district} does not exist in the list.")