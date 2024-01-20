class Animal:

  def eat(self):
    print("This animal is eating")

class Rabbit(Animal):
  def eat(self):
    print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat

# rabbit.eat in this case will use the method inside the Rabbit class, instead of the method in the Animal class.