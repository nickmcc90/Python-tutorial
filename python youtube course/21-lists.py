food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop() # removes the last element from a list
food.insert(0,"cake") # insert a thing at a certain index
food.sort() # this sorts a list alphabetically
food.clear() #removes all the elements from a list


for x in food:
  print(x)