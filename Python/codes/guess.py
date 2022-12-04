import random

random_number = random.randint(1, 10)

count = 1
guesses = 3


print("Guess number from 1 to 10.")

while count <= guesses:

    guess = int(input("Guess: "))

    if guess != random_number:
        if count == guesses:
            print(f"You are out of guesses. Random Number is: {random_number}")
            break
        else:
            count += 1
            continue
    else:
        print(f"You guessed right. ({random_number})")
        break
