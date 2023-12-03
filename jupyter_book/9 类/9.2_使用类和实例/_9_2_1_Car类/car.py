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
        
my_new_car = Car('dog', 'qbk', '20')
print(my_new_car.get_describtion_name())
my_new_car.read_odometer()

## 直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

## 通过方法修改属性的值
my_new_car.update_odometer(44)
my_new_car.read_odometer()

my_new_car.update_odometer(24)

## 通过方法让属性的值递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()