import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    # Computer choice
    comp_choice = random.randint(1, 3)

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))


    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("\nUser choice is:", choice_name)
    print("Computer choice is:", comp_choice_name)

    # Logic For Result
    if choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    ans = input("\nPlay again? (Y/N): ").lower()
    if ans == 'n':
        break

print("Thanks for playing!")