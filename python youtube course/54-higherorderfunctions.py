# functions that can take functions as arguments.

def loud(text):
  return text.upper()

def quiet(text):
  return text.lower()

def hello(func):
  text = func("Hello")
  print(text)

hello(loud) # hello can be called to make the hello text either all uppercase or all lowercase


# part 2!!!!

def divisor(x):
  def dividend(y):
    return y/x
  return dividend

divide = divisor(2)
print(divide(10))