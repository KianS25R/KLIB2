"""KLIB2 libary for machine learning such as rln and more..."""

from kmath import *

def hybrid(z: float) -> float:
    if z <= 0:
        return LeakyReLu(z)
    elif z > 0:
        return ReLu(z)
    
def cz(x: float, w: float, b: float) -> float:
    return x*w+b


class RNN_HYBRID():
    def __init__(self, start: float, target: float, weight: float, weight_layer: float, learnrate: float=0.001):
        super().__init__()
        lr = learnrate
        self.x = start
        self.wx = weight
        self.b = 0
        self.wh = weight_layer
        self.lr = lr
        self.y = target
        self.h = hybrid(cz(start, weight, self.b))
        self.err = (self.h-self.y)
        self.loss = self.err**2
        self.lg = 2*self.err
        self.dhzl = 1.0 if cz(start, weight, self.b) > 0 else 0.1
        self.dLdw = (self.lg)*self.dhzl*start
        self.dLdwh = 0
        self.dLdb = (self.lg)*self.dhzl
        self.wx -= lr*self.dLdw
        self.wh -= lr*self.dLdwh
        self.b -= lr*self.dLdb
        self.memory = 0
    
    def layer(self):
        self.memory = self.h
        self.h = hybrid(self.x*self.wx + self.memory*self.wh + self.b)
        self.err = (self.h-self.y)
        self.loss = self.err**2
        self.lg = 2*self.err
        z = self.x*self.wx + self.memory*self.wh + self.b
        self.dhzl = 1.0 if z > 0 else 0.1
        self.dLdw = (self.lg)*self.dhzl*self.x
        self.dLdwh = (self.lg)*self.dhzl*self.memory
        self.dLdb = (self.lg)*self.dhzl
        self.wx -= self.lr*self.dLdw
        self.wh -= self.lr*self.dLdwh
        self.b -= self.lr*self.dLdb
    
    def run(self, times):
        for i in range(times):
            self.layer()
        print("result: ", self.h)
        print("target: ", self.y)
        print("loss: " ,self.loss)
        print(f"weights: neuron: {self.wx} layer: {self.wh}")
