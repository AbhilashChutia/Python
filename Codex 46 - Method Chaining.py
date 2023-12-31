# Method Chaining
# Calls multiple methods sequentially
# Each call performs an action on the same object and returns itself

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self


    def brake(self):
        print("You step on the brake")
        return self


    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()
car.turn_off()\
        .drive()\
            .brake()\
                .turn_off()