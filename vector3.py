"""script handeling class vector3"""
from kmath import sqrt, deg, atan2

class vector3():
    def __init__(self, x, y, z):
        """creates new vector"""
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return vector3(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return vector3(self.x+other.x, self.y+other.y, self.z+other.z)
    def __mul__(self, other):
        if type(other) == vector3:
            return vector3(self.x*other.x, self.y*other.y, self.z*other.z)
        elif type(other) == float or type(other) == int:
            return vector3(self.x*other, self.y*other, self.z*other)
    def __pow__(self, other):
        return (self.x*other.x)+(self.y*other.y)+(self.z*other.z)
    def length(self):
        """returns length of vector"""
        return sqrt(self.x**2+self.y**2+self.z**2)
    def __truediv__(self, other: float):
        x=self.x/other
        y=self.y/other
        z=self.z/other
        return vector3(x, y, z)
    def angles(self):
        """returns eleveation and direction of 3 dimensional vector"""
        e = deg(atan2(self.y, self.x))
        d = deg(atan2(self.z, self.x))
        return e, d
    def __floordiv__(self, other: vector3):
        x = (self.y*other.z)-(self.z*other.y)
        y = (self.z*other.x)-(self.x*other.z)
        z = (self.x*other.y)-(self.y*other.x)
        return vector3(x, y, z)
    def unit(self):
        """returns unit vector"""
        return self/self.length()