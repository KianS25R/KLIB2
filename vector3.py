"""script handeling class vector3"""
from kmath import sqrt

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
