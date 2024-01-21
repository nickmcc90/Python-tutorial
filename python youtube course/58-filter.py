# filter() = creates a collection of elements from an iterable for which a function returns a true value

# filter(function,iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",21),
           ("Ross",16)]

# let's say we want a list of people who are older than 18 from this list of tuples.

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
  print(i)