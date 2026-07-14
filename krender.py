"""KLIB2 3D rendering """

import KLIB2.kmath as kmath
from KLIB2.vector3 import vector3
from KLIB2.vector2 import vector2

#Formulars

def xback(distance, angle):
    a = kmath.rad(angle)
    theta = kmath.sin_rad(a)
    return distance*theta
    
def yback(distance, angle):
    a = kmath.rad(angle)
    theta = kmath.cos_rad(a)
    return distance*theta
    
class kobject3d():
    def __init__(self, position: vector3=vector3(0,0,0), size: vector3=vector3(1,1,1)):
        super().__init__()
        self.position = position
        self.size = size
        self.cache = []
        
    def update(self):
        self.cache = [vector2(*[self.position.xyz[d]-self.scale[d]/2 for d in range(len(self.position.xyz))])]