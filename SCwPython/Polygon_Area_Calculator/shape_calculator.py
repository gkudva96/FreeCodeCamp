# Class definition for Rectangle shape
class Rectangle:

  # Constructor Method
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  # Function to set the width
  def set_width(self, width):
    self.width = width
  
  # Function to set the height
  def set_height(self, height):
    self.height = height
  
  # Function to get the area
  def get_area(self):
    return self.width * self.height
  
  # Function to get the perimeter
  def get_perimeter(self):
    return 2 * (self.width + self.height)
  
  # Function to get the diagonal
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** (0.5))
  
  # Function to get the pictorial representation
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    pic_string = ""
    for l in range(self.height):
      pic_string += "*" * self.width + '\n'
    return pic_string
  
  # Function to compute how many shapes would fit inside
  def get_amount_inside(self, shape):
    width_fit = (self.width // shape.width)
    height_fit = (self.height // shape.height)
    return width_fit * height_fit
  
  # Function invoked when printing an instance
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# Class definition for Square Shape
class Square(Rectangle):
  
  # Constructor Method
  def __init__(self, side_length):
    super().__init__(side_length, side_length)
  
  # Function to set the side length
  def set_side(self, side_length):
   self.set_width(side_length)
   self.set_height(side_length)
  
  # Function invoked when printing an instance
  def __str__(self):
    return f"Square(side={self.width})"