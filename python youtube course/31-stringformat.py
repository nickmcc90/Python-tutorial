# str.format() = more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item) #this is a sloppy way of writing this string.
print("The {} jumped over the {}".format(animal,item)) # neater
print("The {0} jumped over the {1}".format(animal,item)) # positional argument. animal is index 0 and item is index 1 in the format ().
print("The {yes} jumped over the {no}".format(yes="boon",no="loon")) # keyword args. We can reuse the same argument to, like {yes}  {yes}.

text = "The {} jumped over the {}"
print(text.format(animal,item)) # most elegant.

name = "Nick"

print("Hello, my name is {}".format(name)) # nothing new here
print("Hello, my name is {:10}".format(name)) # this colon and 10 means 10 spaces after the insert.
print("Hello, my name is {:<10}".format(name)) # this left aligns your variable in the space created.
print("Hello, my name is {:>10}".format(name)) # this right aligns your variable in the space created.
print("Hello, my name is {:^10}".format(name)) # this center aligns your variable in the space created.


number = 1000
print("The number pi is {:.2f}".format(number)) # this syntax is to display only the first two decimal points.
print("The number pi is {:,}".format(number)) # this is to add a comma where necessary
print("The number pi is {:b}".format(number)) # this is to have the number in binary
print("The number pi is {:o}".format(number)) # this is to have the number in octal
print("The number pi is {:X}".format(number)) # this is to have the number in hexadeci whatever
print("The number pi is {:e}".format(number)) # this is to have the number in scientific notation