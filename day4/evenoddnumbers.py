# This program prints all odd numbers from 1 to 40.
odd = 1
while odd <= 40:
    print(odd)
    odd += 2
print("These all are odd numbers!")

prime_number = 1
while prime_number <= 40:
    if prime_number > 1:
        for i in range(2, prime_number):
            if (prime_number % i) == 0:
                break
        else:
            print(prime_number)
    prime_number += 1
print("These all are prime numbers!")