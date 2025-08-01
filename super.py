#Super function in OOB


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} color and {'Filled' if self.is_filled else 'Not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.1416 * self.radius * self.radius}cm^2")
        super().describe()
    
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with a area of {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a Triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

circle = Circle(color="White",is_filled= True,radius= 5)
square = Square(color="Blue",is_filled= False,width= 6)
triangle = Triangle(color="Green",is_filled= True,width= 7, height=8)

circle.describe()
square.describe()
triangle.describe()
        