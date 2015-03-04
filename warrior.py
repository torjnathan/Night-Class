
__author__ = 'Nathan'

import random

class Warrior(object):
    """
    attributes:
    name of warrior
    armor to protect with
    weapon to attack with
    life points to track if hte warrior is alive dead, or somewhere in between

    behaviors:
    attack the dragon
    defend himself
    """
    def __init__(self, name):
        self.name = name
        self.armor = "simple shield"
        self.weapon = "basic sword"
        self.life = 100

    def attack(self, target):
        target.life = target.life - 10

    def defend(self):
        self.life = self.life + 10

class Dragon(object):
    """
    attributes:
    name of the dragon
    weapon to attack with
    life points (same as above)

    behaviors:
    attack the warrior
    defend himself
    """
    def __init__(self, name):
        self.name = name
        self.weapon = "fire breath"
        self.life = 100

    def attack(self, target):
        target.life -= 10

    def defend(self):
        self.life += 10


def armor_room():
    print "This room has plenty of shields in it.  I recommend you take up a shield...like, NOW!."
    print "-" * 100
    print "Do you choose to take up a shield?"

    armor = raw_input("Yes, No: ")
    if armor == "yes":
        print "Nice! This shield protected you, you get to live!"
        exit(0)
    elif armor == "no":
        print "You have no armor on and the dragon burned you to a crisp!"
        exit(0)
    else:
        print "I don't know what you mean...?!?"


def weapon_room():
    print "-" * 100
    print "Look at all of the swords in this room!!"
    print "Choose a sword from any wall in the room... you're enemy, the dragon is coming..."
    print "Did you choose a sword?"
    print "-" * 100

    while True:
        choice = raw_input("> ")
        if choice == "yes":
            player.weapon = "Amazing Claymore"
            print "You just picked up an " + player.weapon
            # dragon.attack()
            done("chaaarrrgggeee...")
        elif choice == "no":
            print "-" * 100
            print "Watch out he's coming at you..do you have armor for protection?"
            dragon.weapon = "fire breath"
            print "Dragon is breathing " + dragon.weapon
            armor_room()
        else:

            print "I don't understand what that means."
            exit(0)

def library_room():
    print "-" * 100
    print "Here you see a great library with many books."
    print "The Dragon followed you, but if you read to him, you may put him to sleep!"
    print "Do you choose to 'run' for your life, or do you rather choose to 'read' the dragon to sleep?"
    print "-" * 100

    choice = raw_input("> ")

    if "run" in choice:
        done("You're out of here!")
    elif "read" in choice:
        done("Sleepy sleepy Dragon. Phew! You're safe!")
    else:
        library_room()


def done(why):

    print why, "Thanks for playing."
    exit(0)

def start_game():
    print "-" * 100
    print "You are in a dark room."
    print "There is a door to your 'right' and 'left', or you may choose to keep walking 'straight ahead'"
    print "Which one do you choose to enter?"
    print "-" * 100

    choice = raw_input("> ")

    if choice == "left":
        weapon_room()
    elif choice == "right":
        library_room()
    elif choice == "straight ahead":
        done("You have chosen to chicken out!")
    else:
        done("That was not an option. You have chosen to exit.")

warrior_name = raw_input("Name your warrior: ")
player = Warrior(warrior_name)
dragon_name = raw_input("Name your Dragon: ")
dragon = Dragon("Dragonius")

start_game()

