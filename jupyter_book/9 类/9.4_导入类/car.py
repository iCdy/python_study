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

class Battery:
    def __init__(self, battery_size=40):
        self.battery = battery_size
    
    def describe_battery(self):
        print(f"battery size: {self.battery}")
    
    def get_range(self):
        print(f"{self.battery * 4.5}")
        
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(model, make, year)
        self.battery = Battery()