from abc import ABC, abstractmethod


class Vehicle:
    __SEASON = 'summer'
    _AC_FUEL_CONSUMPTION = 0  # liters / km
    _FUEL_RETAIN_COEFFICIENT = 1  # unitless

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity  # liters
        self.fuel_consumption = fuel_consumption  # liters / km

    def drive(self, distance):
        consumed_fuel = (self.fuel_consumption + self._AC_FUEL_CONSUMPTION) * distance
        if self.fuel_quantity < consumed_fuel:
            return
        self.fuel_quantity -= consumed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += self._FUEL_RETAIN_COEFFICIENT * fuel


class Car(Vehicle):
    _AC_FUEL_CONSUMPTION = 0.9  # liters / km
    _FUEL_RETAIN_COEFFICIENT = 1  # unitless


class Truck(Vehicle):
    _AC_FUEL_CONSUMPTION = 1.6  # liters / km
    _FUEL_RETAIN_COEFFICIENT = 0.95  # unitless


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
