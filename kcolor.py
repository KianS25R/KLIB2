"""color module for KLIB2"""


## imports ##

from vector3 import vector3

## class ##

class Color3():
    def __init__(self, vector: vector3):
        super().__init__()
        self.r = vector.x
        self.g = vector.y
        self.b = vector.z
    
    def to_hex(self) -> str:
        return f"#{(hex(self.r)).removeprefix("0x")}{(hex(self.g)).removeprefix("0x")}{(hex(self.b)).removeprefix("0x")}"
