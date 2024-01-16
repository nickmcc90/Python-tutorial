import time

for i in range(10): # range(10) is 0 through 9. 10 is exclusive
  print(i+1)

for i in range(50,100): # 50 is inclusive 100 is exclusive
  print(i+1)

for i in range(50,100,2): # prints 50, 52, 54 etc
  print(i)

for i in "bro code": #iterates through a name and prints each letter
  print(i)


#range(starting point, ending point, count by)



for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("Happy New Year!")