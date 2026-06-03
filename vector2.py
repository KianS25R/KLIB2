"""script handeling class vector2"""
from kmath import sqrt, atan, deg
class vector2():
    def __init__(self, x: float, y: float):
        """creates new vector"""
        super().__init__()
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other):
        return vector2(self.x+other.x, self.y+other.y)
    def __mul__(self, other):
        if type(other) == vector2:
            return vector2(self.x*other.x, self.y*other.y)
        elif type(other) == float or type(other) == int:
            return vector2(self.x*other, self.y*other)
    def __sub__(self, other):
        return vector2(self.x-other.x, self.y-other.y)
    def length(self):
        """returns length of vector"""
        return sqrt(self.x**2+self.y**2)
    def across(self):
        """returns cross vector"""
        return vector2(-self.y, self.x)
    def unit(self):
        """returns unit for vector"""
        return vector2(self.x/self.length(),self.y/self.length())
    def __pow__(self, other):
        return (self.x*other.x)+(self.y*other.y)
    def angle(self):
        """returns angle for vector2"""
        if self.x != 0:
            return deg(atan(self.y/self.x))
        elif self.x == 0:
            return 90