import random
print(Number Guessing Game)
number = random.randint(1, 9)
chance  = 0
print("Guess a number (between 1 and 9):")

while chance < 5:

    guess = int(input("Enter your guess :-"))


    if guess == number:
    print("Congratulations! YOU WON!!!")
    break

    elif guess < number:
    print("Your guess was too low: Guess a number higher than", guess)

    else guess > number:
    print("Your guess was too high: Guess a number lesser than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE!! The number is", number)