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