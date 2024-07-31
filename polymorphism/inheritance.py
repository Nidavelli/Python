class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year=year
    def move(abc):
        print("Moving")
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def move(abc):
        print("Driving")
class Boat(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def move(abc):
        print("Sailing")
class Plane(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def move(abc):
        print("Flying")
        
car1=Car("Ford","Mustang",2018)
boat1=Boat("Ibiza","Touring 20",2002)
plane1=Plane("Boeing","747",2024)

for x in (car1,boat1,plane1):
    x.move()