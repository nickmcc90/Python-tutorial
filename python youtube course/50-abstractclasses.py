from abc import ABC, abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def go(self):
    pass

class Car(Vehicle):

  def go(self):
    print("You drive the car")

class Motorcycle(Vehicle):
  

  def go(self):
    print("You ride the motorcycle")


# we dont want people making objects from the vehicle class, so we add the syntax that you see above.
# each of the child classes is overriding the go method. This needs to happen with abstract methods. They need to be overridden.