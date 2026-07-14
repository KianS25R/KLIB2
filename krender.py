"""KLIB2 3D rendering """

import KLIB2.kmath as kmath

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
    def __init__(self):
        super().__init__()