class HelloWorld:
    def greet(self, name):
        print("Hi {}, Welcome to the object world! ". format(name))

name = input("Enter your name : ")
greeter = HelloWorld
greeter.greet(name)
        