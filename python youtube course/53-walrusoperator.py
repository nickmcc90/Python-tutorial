#walrus opertor = assigns values to variables as part of a larger expression

happy = True
print(happy)
#this is the long way

print(happy := True)

#here is a more practical way of application

foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
    break
  foods.append(food)

# you can write this code using the walrus operator
  
foods = list()
while food := input("What food do you like?: ") != "quit":
  foods.append(food)