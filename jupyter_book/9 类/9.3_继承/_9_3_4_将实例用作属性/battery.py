class Battery:
    def __init__(self, battery_size=40):
        self.battery = battery_size
    
    def describe_battery(self):
        print(f"battery size: {self.battery}")
    
    def get_range(self):
        print(f"{self.battery * 4.5}")