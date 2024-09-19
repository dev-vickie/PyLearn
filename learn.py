class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self,side_length):
        self.side_length = side_length
    def area(self):
        return super().area()
    
    
