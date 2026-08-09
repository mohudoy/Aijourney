person = {"name": "Alice", "age": 30, "city": "New York", "f/n": "mr. jack", "a/c": "000345789", "last trn date": "15/07/2021", "last trn amount": 5000, "last trn type": "debit", "last trn status": "successful"}
print("Person dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
add_key = input("Enter a key to add: ")
add_value = input("Enter a value for the key: ")
person[add_key] = add_value
print("Person dictionary after adding the new key-value pair:")
for key, value in person.items():
    print(f"{key}: {value}")