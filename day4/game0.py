secret_number = 6
guess = int(input("Guess a number(1-10): "))

if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number:
    print("Your guess is low. Try again.")
    guess = int(input("Guess a number(1-10): "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, that's not the correct number. The secret number was", secret_number)
elif guess > secret_number:
    print("Your guess is high. Try again.")
    guess = int(input("Guess a number(1-10): "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, that's not the correct number. The secret number was", secret_number)