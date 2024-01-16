# nested loops = inner loop finishes all its iterations before it gets to the outer loop. Time stamp 1:14:27

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in rows:
  for j in columns:
    print(symbol, end="") # the end here makes it so that it doesn't go to a next line.
  print()   # this creates a new line.