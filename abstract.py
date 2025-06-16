#abstract class method in OOB
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go (self):
        pass

    @abstractmethod
    def stop (self):
        pass

class Car(Vehicle):
    def go (self):
        print("You're going too fast !")

    def stop (self):
        print("Stop the car.")
class Bike(Vehicle):
    def go (self):
        print("You're going too fast !")
    def stop (self):
        print("Stop the Bike.")

car = Car()
car.go()
car.stop() 
bike= Bike()
bike.go()
bike.stop()