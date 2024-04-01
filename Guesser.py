import random

incorrect = True

print("Number Guesser")
cpu = random.randint(1, 100)

while incorrect:
    player = int(input("Input your guess: "))

    if player == cpu:
        print("You guessed correctly")
        incorrect = False

    elif player > cpu:
        print("Guess lower!")

    else:
        print("Guess Higher")
