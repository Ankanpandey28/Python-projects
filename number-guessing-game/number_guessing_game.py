import random
print("Welcome to the number guessing game!\nYou have 5 chances to guess the number.Let's start!")

lower=int(input("Enter the lower bound:"))
upper=int(input("Enter the upper bound:"))

print(f"You have 5 chances to guess the number between {lower} and {upper}.")

num=random.randint(lower,upper)
chan=5
guess=0

while guess<chan:
    guess+=1
    guess_num=int(input("Enter your guess number:"))
    
    if guess_num==num:
        print(f"Correct! The number is {num}.You guessed the number in {guess} attempts.")
        break
    elif guess==chan and guess_num!=num:
        print(f"The number was {num}.Better luck next time!")
    elif guess_num>num:
        print("Too high! Try a lower value")
    else:
        print("Too low! Try a higher value")
