#
#
#
import random

user_1 = 'start'

def intro():
    print("""
    Hello, This is a rock, paper, scissors game.
    I will ask you to type in one of the
    three using the first letter,
    and then the computer will choose one, and compare
    to see who the winner is.
    """)

    user = input("> ")
    user_in = user.upper()

    return user_in

#---------------------------------------------#

if user_1 != ('ROCK') and user_1 !=('PAPER') and user_1 !=('SCISSORS'):
    user_1 = intro()



user_2 = user_1.upper()
comp_in = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
print("-" * 10)
print(f" You chose: {user_2} \nThe computer chose: {comp_in}\n")


if user_2 == comp_in:
    print("It's a tie")

elif user_2 == 'ROCK':
    if comp_in == 'PAPER':
        print("YOU lose.")
    elif comp_in == 'SCISSORS':
        print("You win.")
    else:
        print("Something went wrong.")

elif user_2 == 'PAPER':
    if comp_in == 'SCISSORS':
        print("You lose")
    elif comp_in == 'ROCK':
        print("You win.")
    else:
        print("Something went wrong.")

elif user_2 == 'SCISSORS':
    if comp_in == 'ROCK':
        print("You lose")
    elif comp_in == 'PAPER':
        print("You win.")
    else:
        print("Something went wrong.")
else:
    print("SOmething went wayy wrong")






