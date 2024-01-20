class Car:
    #classes have attributes and methods. Attributes of cars are as shown, and methods are functions

    def __init__(self,make,model,year,color): #this is a special method that creates objects. It's called a constructor.
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self): # self is any object that we are using for this class.
        print("This "+self.model+ " is driving")

    def stop(self):
        print("This car has stopped")


car_1 = Car("Chevy","Corvette",2021,"blue")

car_1.drive()
car_1.stop()

print(car_1.make)