class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")
    def sleep(self):
        print(f"{self.name} is sleeping!")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")

class Rabit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabit = Rabit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.hunt()

