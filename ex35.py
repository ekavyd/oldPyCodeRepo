#
#
#

from sys import exit

def gold_room():
    print("\nThis room is full of 1000 gold, How much do you take?")
    choice = int(input("> "))

    if  choice > 0 and  choice < 1100:
        how_much = choice
    else:
        dead("Man, learn to type a number.")

    if how_much<50:
        print("\n\t\tNice, you're not greedy, you win!!!!!!!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("\nThere is a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("You can: \n\n(taunt bear) \n(take honey) \n(open door) *if bear has moved")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. ")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("\nHere you see the great evil Cthulhu. ")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you (flee) for your life or eat your (head)?")

    choice = input(" >")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        dead("Wrong answer.")

def dead(why):
    print(why, "YOU HAVE DIED!\n\n")
    exit(0)

def start():
    print("\nYou are in a dark room.")
    print("There is a door to your (right) and to your (left).")
    print("Which do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
















