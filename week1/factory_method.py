class Car:
    def drive(self):
        return "Driving Car"

class Bike:
    def drive(self):
        return "Driving Bike"

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()

vehicle1 = VehicleFactory().create_vehicle("car")
vehicle2 = VehicleFactory().create_vehicle("bike")

print(vehicle1.drive())
print(vehicle2.drive())