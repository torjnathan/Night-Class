__author__ = 'Nathan'

                    ########################02/19/2015###########################

class MyCritter(Animal):
    critter_proxy = Critter()
    critter_proxy.__dict__
    critter_proxy.tail
    critter_prox.run()
    def __init__(self):
            self.species = critter_proxy

# you can use this in a 'for' loop

class AnimalFactory(object):
    def make_animal(self, name, color, food, predator):
        animal = Animal()
        animal.name = name
        animal.color = color
        animal.food = food
        animal.predators = predator
        return animal

    factory = AnimalFactory()
    bear = factory.make_animal("bear", "brown", "fish", "hunters")

class MainFactory(object):
    def make_mains(self, x, y, z):
        obj = Main()
        obj.x = x
        obj.y = y
        obj.z = z
        return obj
factory = MainFactory()
main0 = factory.make_mains(1,2,3)
main1 = factory.make_mains(1,2,3)
main2 = factory.make_mains(1,2,3)
