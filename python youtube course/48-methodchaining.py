#method chaining = calling multiple methods sequentially, each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You start driving")
        return self

    def brake(self):
        print("You start to brake")
        return self

car_1 = Car()

#instead of...
car_1.turn_on
car_1.drive
#we do.... (but you need to have "return self" in the method)
car_1.turn_on().drive()
# if you want them on different lines, do..
car_1.turn_on()\
      .drive()