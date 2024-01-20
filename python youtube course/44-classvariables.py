#diff between class and instance variables
# instance variable is inside the constructor
# class variable is made globally in the class

from 43-objectorientedprogramming import Car

car_1 = Car("Chevy","Corvette",2021,"blue")

car_1.make

print(Car.wheels) # wheels is a class variable that can be referenced just by using the class

#you are able to change class variables