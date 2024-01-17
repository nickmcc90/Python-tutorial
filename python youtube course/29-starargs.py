# args = parameter that will pack all arguments into a tuple. A function can accept a varying amount of arguments.
# timestamp is 2:13:37

def add(nums1,nums2):
  return nums1 + nums2

print(add(1,2))     #what if we wanted to have a random number of arguments?

def add(*args):
  sum = 0
  for i in args:
    sum += i
  return sum

print(add(1,2,3,4,5))       #this can be as many arguments as you want

# in tuples, you can't change any numbers. But we can type cast the tuple, then change.

def add(*args):
  sum = 0
  args = list(args)
  args[0] = 7
  for i in args:
    sum += i
  return sum

print(add(1,2,3,4,5,6,7)) # this function changes the first element in the tuple to a 7.
