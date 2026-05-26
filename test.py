from vector import *
import agurk as pickle


a = vector2(0,1)
b = a.cross()
print(b.x, b.y)

print(b.angle(), a.angle())