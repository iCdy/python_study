from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.battery = Battery()
    
my_leaf = ElectricCar("qbk", 'cdy', 2023)
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()