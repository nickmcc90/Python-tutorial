class Car:

  color = None

# this function is out of the class
def change_color(vehicle,color):
  
  vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

print(car_1.color)

#this should just have no color.

change_color(car_1, "white")

print(car_1.color)

# this changes the color