import random

x = random.randint(1,6) # this generates a random int between the nums provided.
y = random.random() # this generates a random float from 0 through 1

myList = ['rock','paper','scissors']
z = random.choice(myList) # This generates a random choice.

print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards) # this should have a different order now