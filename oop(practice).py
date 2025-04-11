
class Circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def area(self):
        return 3.14*self.r*self.r
    
circle1 = Circle(0,0,1)
print(circle1.area())
    
    
        