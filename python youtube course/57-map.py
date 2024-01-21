# map applies a function to each item in an iterable

# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

# we need something to change the prices to euros. Our function can be a lambda

to_euros = lambda data: (data[0],data[1]*0.82)

store_euros = list(map(to_euros,store))

# this will make a new list/store of the new prices.