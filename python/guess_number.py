import random

limit = input("\nType a number: ")

if limit.isdigit():
    limit = int(limit)

    if limit <= 0:
        print('\nPlease type a number larger than 0 next time:')
        quit()
else:
    print('\nPlease type a number:')
    quit()

random_number = random.randint(0, limit)
attempts = 0

while True:
    attempts += 1
    user_guess = input("\nMake a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('\nPlease type a number next time:')
        continue

    if user_guess == random_number:
        print("\n   You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("\n   You got it in", attempts, "guesses")