"""KLIB2 libary for machine learning such as rln and more..."""

from .kmath import *
from agurk import write, read

def hybrid(z: float) -> float:
    if z <= 0:
        return LeakyReLu(z)
    elif z > 0:
        return ReLu(z)
    
def cz(x: float, w: float, b: float) -> float:
    return x*w+b


class RNN_HYBRID():
    def __init__(self, start: float, target: float, neurons: int, load_model: str="", learnrate: float=0.001):
        super().__init__()
        if load_model == "":
            self.gen = random(953674, -(1/sqrt(neurons)), (1/sqrt(neurons)))
            lr = learnrate
            self.wx = [self.gen() for i in range(0,neurons)]
            self.amount = neurons
            self.b = [0 for i in range(0,neurons)]
            self.wh = [[self.gen() for j in range(neurons)] for i in range(neurons)]
        else:
            lr = learnrate
            data = read(load_model)
            self.wx = [float(x) for x in data[0]]
            self.b = [float(x) for x in data[1]]
            self.wh = [[float(x) for x in row] for row in data[2]]
            self.amount = len(self.wx)
        self.h = [0 for i in range(0,self.amount)]
        self.x = start
        self.lr = lr
        self.y = target
        self.err = [0 for i in range(0, self.amount)]
        self.loss = [0 for i in range(0, self.amount)]
        self.lg = [0 for i in range(0, self.amount)]
        self.dhzl = [0 for i in range(0, self.amount)]
        self.dLdb = [0 for i in range(0, self.amount)]
        self.dLdw = [0 for i in range(0, self.amount)]
        self.dLdwh = [[0 for j in range(self.amount)] for i in range(self.amount)]
        self.memory = [0 for i in range(0, self.amount)]
    
    def layer(self):
        for i in range(0, self.amount):
            self.memory[i] = self.h[i]
            total = self.wx[i]*self.x
            for j in range(0, self.amount):
                total += self.wh[i][j]*self.memory[j]
            total += self.b[i]
            self.h[i] = hybrid(total)
            self.err[i] = (self.h[i]-self.y)
            self.loss[i] = self.err[i]**2
            self.lg[i] = 2*self.err[i]
            self.dhzl[i] = 1.0 if total > 0 else 0.1
            self.dLdw[i] = (self.lg[i])*self.dhzl[i]*self.x
            for j in range(0, self.amount):
                self.dLdwh[i][j] = (self.lg[i])*self.dhzl[i]*self.memory[j]
                self.wh[i][j] -= self.lr*self.dLdwh[i][j]
            self.dLdb[i] = (self.lg[i])*self.dhzl[i]
            self.wx[i] -= self.lr*self.dLdw[i]
            self.b[i] -= self.lr*self.dLdb[i]
    
    def run(self, times):
        for i in range(times):
            self.layer()
        print("result: ", self.h[self.loss.index(min(self.loss))])
        print("target: ", self.y)
        print("loss: " ,min(self.loss))
        print(f"weights: neuron: {self.wx[self.loss.index(min(self.loss))]} layer: {self.wh[self.loss.index(min(self.loss))]}")
        a = input("Would you like to save as model? (Y/N): ")
        if a == "Y":
            c = input("Filename: ")
            write([self.wx, self.b, self.wh], f"{c}.mem")