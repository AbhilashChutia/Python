# Multiple Inheritance
# When a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")

class Predetor:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass

class Fish(Prey, Predetor):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()