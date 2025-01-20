# Parent class
class vehicle:
    def sound(self):
        return "Vehicle engine starting"
    
# Child class 1 Car

class car(vehicle):
    def sound(self):
        return "Car engine is starting"
    
# child class 2 Motorcycle

class motorcycle(vehicle):
    def sound(self):
        return "Motorcycle engine is starting"

# child class 3 Truck

class truck(vehicle):
    def sound(self):
        return "Truck engine is starting"
    
vehicles = [vehicle(), car(), motorcycle(), truck()]

for v in vehicles:
    print(v.sound())