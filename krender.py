"""KLIB2 3D rendering """

import KLIB2.kmath as kmath
from KLIB2.vector3 import vector3

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
    def __init__(self, position: vector3=vector3(0,0,0)):
        super().__init__()
        self.position