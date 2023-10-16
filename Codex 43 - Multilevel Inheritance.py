# Multi Level Inheritance
# When a derived class inherits another derived class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("this dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()