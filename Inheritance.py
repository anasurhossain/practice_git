#Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is asleep")
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQEEK!")

dog = Dog("Scooby")
cat = Cat("Uchia")
mouse = Mouse("Miky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()
cat.speak()
mouse.speak()