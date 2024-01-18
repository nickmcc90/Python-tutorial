import os

#source is location of test file
#destination is where you want it to go.

source = ""
destination = ""


try:
  if os.path.exists(destination):
     print("There's something there already")
  else: 
     os.replace(source,destination)
     print(source+" was moved")
    

except FileNotFoundError:
    print(source+"not found")