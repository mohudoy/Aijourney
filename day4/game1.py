secret_number = 6
guess = int(input("Guess a number(1-10): "))

while guess != secret_number:
    if guess < secret_number:
        print("Your guess is low. Try again.")
    else:
        print("Your guess is high. Try again.")
    guess = int(input("Guess a number(1-10): "))
print("Congratulations! You guessed the correct number.")