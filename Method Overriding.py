class Vehicle:
    def StaticRange(self):
        print("Vehicle Started")

class Car(Vehicle):

    def start(self):
        print("Car Started")

c = Car()

c.start()