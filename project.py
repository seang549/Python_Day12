import random
from art import logo
chosen_number = random.randint(0,100)

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()

def compare(num):
    while num > 0:
        print(f"You have {num} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("It has to be a number. For Example: '79'")
            continue
            
        if int(guess) > chosen_number:
            print("Too high.")
            num -= 1
            if num == 0:
                print("You lose")
        elif int(guess) < chosen_number:
            print("Too low")
            num -= 1
            if num == 0:
                print("You lose")
        else:
            print(f"You got it! The answer was {chosen_number}")
            break

if difficulty == "easy":
    attempts = 10
    compare(attempts)
elif difficulty == "hard":
    attempts = 5
    compare(attempts)
else:
    print("That was not an option.\n Goodbye")

    
