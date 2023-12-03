class Car:
    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0
    
    def get_describtion_name(self):
        long_name = f"{self.model.title()} {self.make.title()} {self.year.title()}"
        return long_name
    
    def read_odometer(self):
        print(f"odometer: {self.odometer_reading}")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("error")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    def fill_gas_tank(self):
        print("ok filled")
        
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.battery_size = 40
    
    def describe_battery(self):
        print(f"battery_size: {self.battery_size}")
        
    def fill_gas_tank(self):
        print('sorry, no tank')
        
my_leaf = ElectricCar("qbk", 'cdy', '2023')
print(my_leaf.get_describtion_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()