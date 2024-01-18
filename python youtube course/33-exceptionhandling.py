# exception = events detected during execution that interrupt the flow of a program

# it's good practice to wrap dangerous code in a "try" block.

# pick up back at 2:42:00

try:
  numerator = int(input("Enter a number to divide: "))
  denominator = int(input("Enter a number to divide by: "))
  result = numerator / denominator
  print(result)
except: ZeroDivisionError as e: # this 'as e' syntax allows us to capture the error and print it out along with the explanation given.
    print(e)
    print("you can't divide by zero!!")
except ValueError as e:
    print(e)
    print("enter only real numbers please")
except Exception as e: # it's not good to have a single exception block to handle all exceptions. Make a special case for all exceptions.
    print(e)
    print("something went wrong :(")
else:
    print(result)   # if there's no exceptions, then we can print the result
finally:
    print("This will always execute")
