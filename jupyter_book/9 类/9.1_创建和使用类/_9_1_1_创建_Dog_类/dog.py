class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name.title()} is now sitting")
    
    def roll_over(self):
        print(f"{self.name.title()} rolled over")
        
my_dog = Dog("qbk", 20)
print(f'{my_dog.name} is my dog, it is {my_dog.age} years old')

my_dog.sit()

your_dog = Dog("lxn", 20)
your_dog.roll_over()