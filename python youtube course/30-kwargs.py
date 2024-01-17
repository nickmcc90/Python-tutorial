# **kwargs = parameter that packs all arguments into a dictionary.
# useful so that a function can accept a varying amount of keyword arguments.

def hello(first, last):
  print("Hello "+ first + " " + last)

hello(first="Bro",middle="Dude",last="Code") # in this function, middle isn't accepted. **kwargs can help.



def hello(**kwargs):
  print("Hello "+ kwargs['first'] + " " + kwargs['last'])

hello(first="Bro",middle="Dude",last="Code") # this should work now. But what if they type in a lot of names?


def hello(**kwargs):
  print("Hello",end=" ")
  for key,value in kwargs.items():
    print(value,end=" ")

hello(first="Bro",middle="Dude",last="Code") # this should print any number of arguments.