#super() = 

class Rectangle:
  pass

class Square(Rectangle):

  def __init__(self, length, width):
    self.length = length
    self.width = width

class Cube(Rectangle):

  def __init__(self, length, width, height):
    self.length = length
    self.width = width
    self.height = height



# so instead of having to rewrite the self.length and self.width for each of these child classes, we can have the init method
# inside of the parent class and use the super() inside of the child classes.
    
class Rectangle:

  def __init__(self, length, width):
    self.length = length
    self.width = width


class Square(Rectangle):

  def __init__(self, length, width):
    super().__init__(length,width)

  def area(self):
    return self.length*self.width


class Cube(Rectangle):

  def __init__(self, length, width, height):
    super().__init__(length,width)
    self.height = height

  def volume(self):
    return self.length*self.width*self.height
  
square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())


