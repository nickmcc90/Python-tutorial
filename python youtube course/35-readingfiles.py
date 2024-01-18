with open('35a-textfile.txt') as file:
  print(file.read()) # this closes any files after opening them. It doesn't catch exceptions though.

try:
  with open('35a-textfile.txt') as file:
    print(file.read())

except FileNotFoundError:
  print("Wasn't found :(")