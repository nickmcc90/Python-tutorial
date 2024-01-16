# slicing = create a substring by extracting elements from another string
#         indexing[] or slice()
#         [start:stop:step]
name = "Bro Code"

first_name = name[0:3] #this should print Bro
first_name = name[:3] #this also prints Bro
last_name = name[4:8] #this should print Code
last_name = name[4:] #this should also print Code

print(first_name)

funky_name = name[0:8:2] #this prints BoCd because of the step
funky_name = name[::2] #this also prints BoCd because of the step

reversed_name = name[::-1] #this returns a reversed string


website = "http://google.com"

slice = slice(7,-4) # prints google. Negative index starts from the right
print(website[slice])


