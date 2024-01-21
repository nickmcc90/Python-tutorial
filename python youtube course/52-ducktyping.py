class Duck:
  def walk(self):
    print("The duck is walking")

class Chicken:
  def walk(self):
    print("The chicken is walking")

class Person():
  def catch(self, duck):
    duck.walk()
    print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
#this should work
person.catch(chicken)
#this should also work, because chicken and duck have the same .walk function.
#if chicken were to stop having this .walk function, it wouldn't work