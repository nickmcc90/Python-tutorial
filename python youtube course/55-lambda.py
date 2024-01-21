# useful if you need a function for a short amount of time

# lambda parameters:expression


def double(x):
  return x*2

print(double(5))

#this is the long way to write it ^
#this is the lambda way v

double = lambda x:x*2
print(double(5))

multiply = lambda x, y: x*y
print(multiply(5,6))

# complex situation

age_check = lambda age:True if age >= 18 else False
print(age_check(14))