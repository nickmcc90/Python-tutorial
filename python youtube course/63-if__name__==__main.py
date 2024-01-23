# python will assign the __name__ variable a value of '__main__' if it's the inital module being run

import module_two
print(__name__) # this should be equal to main since we are in the main module
print(module_two.__name__) # this should be equal to the imported module name since we are importing it

# if __name__ == __main__, basically the module in question is being run directly instead of indirectly

def main():
  # allllllllll the code here
  return "yuh"


if __name__ == '__main__':
   main()