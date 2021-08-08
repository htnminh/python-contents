import math 


class Figure:
    def perimeter(self):
        pass
    
    def area(self):
        pass


class LengthException(Exception):
    pass
class InvalidTriangleException(Exception):
    pass

    
class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            if width > 0 and height > 0:
                self.width = width
                self.height = height
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return (self.width + self.height) * 2
    def area(self):
        return self.width * self.height
        
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height    
        
        
class Circle(Figure):
    def __init__(self, radius):
        try:
            if radius > 0:
                self.radius = radius
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
    
class Triangle(Figure):
    def __init__(self, a, b, c):
        try:
            if a > 0 and b > 0 and c > 0:
                if a + b > c and b + c > a and a + c > b:
                    self.a = a
                    self.b = b
                    self.c = c
                else:
                    raise InvalidTriangleException
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
        except InvalidTriangleException as e:
            print(str(type(e)) + ' was raised')
            
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        a, b, c = self.a, self.b, self.c
        return math.sqrt(4 * a**2 * b**2 - (a**2 + b**2 - c**2)**2) / 4
        
    # S = h*a/2   2S = ha    h = 2S/a
    def get_height_a(self): 
        return 2 * self.area() / self.a 
    def get_height_b(self):
        return 2 * self.area() / self.b
    def get_height_c(self):
        return 2 * self.area() / self.c
      
class Square(Rectangle):
    def __init__(self, side_length):
        Rectangle.__init__(self, side_length, side_length)
        
    def set_width(self, new_side):
        self.width = new_side
        self.height = new_side
    def set_height(self, new_side):
        self.set_width(new_side)