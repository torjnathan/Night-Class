__author__ = 'Nathan'

__author__ = 'Nathan'

class Warrior(object):
    def __init__(self, name, weapon, shield):
        self.name = name
        self.weapon = weapon
        self.shield = shield

    def attack(self, attack_dragon):
        pass

    def defense(self, defense_dragon):
        pass


class Dragon(object):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, attack_warrior):
        pass

    def defense(self, defense_warrior):
        pass

    def life(self, life_level):
        pass

w_name = 'Drake'
w_weapon = 'sword'
w_armor = 'shield'

warrior = Warrior (w_name, w_weapon, w_armor)

d_name = 'Pete'
d_weapon = 'fire'

dragon = Dragon (d_name, d_weapon)


print "---------------------------------------"
print("You're in a room facing a fierce, huge dragon!")
print("What do you choose to do?")
print "---------------------------------------"
print("Press 1 to start the fight!")


def fight():
    print("Let's go to battle... don't be discouraged, but your enemy is huge")
    print("First, choose protection or weapon")
    print("Choose Shield or Sword")

    while True:
        enter= raw_input()

    if enter == "1":


# if enter =="2":
# print("Press 2 to run for your life")