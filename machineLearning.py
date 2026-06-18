"""KLIB2 libary for machine learning such as rln and more..."""

from KLIB2.kmath import *
from KLIB2.agurk import write, read
from KLIB2.lm_core import activate_step

def hybrid(z: float) -> float:
    if z <= 0:
        return LeakyReLu(z)
    elif z > 0:
        return ReLu(z)
    

def hybrid_prime(z):
    if z <= 0:
        return 0.01
    else:
        return 1


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

class RNNLM_HYBRID():
    def __init__(self, vocab_size: int, dictionary: str, veclength: int = 32, load_vocab: str = "no", seed: int = 564963, neurons: int = 128, lr: float=0.001):
        super().__init__()
        self.genrandd = random(seed,-(1/sqrt(veclength)), 1/sqrt(veclength))
        self.genrandn = random(seed, -(1/sqrt(neurons)), 1/sqrt(neurons))
        self.__warm = False
        self.lr = lr
        self.__wordstohandle = []
        if load_vocab != "no":
            self.embedings = read(f"{load_vocab}/embed.mem")
            self.vocabL = read(f"{load_vocab}/info.meta")[0]
            self.vecL = read(f"{load_vocab}/info.meta")[1]
            self.neurons = read(f"{load_vocab}/info.meta")[2]
            self.bias = read(f"{load_vocab}/bias.mem")
            self.lhweights = read(f"{load_vocab}/lhweights.mem")
            self.lweights = read(f"{load_vocab}/lweights.mem")
            self.dictionary = read(f"{load_vocab}/dict.mem")
            self.who = read(f"{load_vocab}/who.mem")
            self.bo = read(f"{load_vocab}/bo.mem")
            self.ht = read(f"{load_vocab}/info.meta")[3]
            print(self.embedings)
        else:
            self.neurons = neurons
            self.embedings = [[self.genrandd() for i in range(veclength)] for j in range(vocab_size)]
            self.lweights = [[self.genrandd() for i in range(veclength)] for j in range(neurons)]
            self.lhweights = [[self.genrandn() for i in range(neurons)] for j in range((neurons))]
            self.bias = [0 for i in range(neurons)]
            self.who = [[self.genrandn() for i in range(neurons)] for j in range(vocab_size)]
            self.bo = [0 for i in range(vocab_size)]
            self.vocabL = vocab_size
            self.vecL = veclength
            self.dictionary = read(dictionary)
            self.ht = [0 for i in range(neurons)]
    
    def warmup(self, sentence: str):
        """use only once!!!"""
        if self.__warm != True:
            print("Warming Model for use!")
            self.__warm = True
            split = sentence.split(" ")
            self.__wordstohandle = split
            self.reply = []
        else:
            raise Exception("Attempted double warmup dont fucking do this!")
        
    def __activate(self, indexa, target):
        activate_step(self, indexa, target)
        




    def __getstuff(self, word: str):
        return list.index(self.dictionary, word)

    def run(self, times: int, f:str ="", s:str = ""):
        if f != "" and s != "":
            for i in range(times):
                self.__activate(self.__getstuff(f), self.__getstuff(s))
        else:
            for j in range(times):
                for i in range(len(self.__wordstohandle)-1):
                    self.__activate(self.__getstuff(self.__wordstohandle[i]), self.__getstuff(self.__wordstohandle[i+1]))
                self.reply.insert(0, self.dictionary[self.__getstuff(self.__wordstohandle[i])])
                print(*self.reply)
                self.reply.clear()

    def train(self, turns: int):
        for i in range(turns):
            for h in range(self.vocabL):
                for j in range(self.vocabL):
                    self.__activate(h, j)
                    print("word1:", self.dictionary[h],"target:" , self.dictionary[j])
        write(self.embedings, "test/embed.mem")
        write([self.vocabL, self.vecL, self.neurons, self.ht], "test/info.meta")
        write(self.bias, "test/bias.mem")
        write(self.lhweights, "test/lhweights.mem")
        write(self.lweights, "test/lweights.mem")
        write(self.dictionary, "test/dict.mem")
        write(self.who, "test/who.mem")
        write(self.bo, "test/bo.mem")
        print(self.loss)
        print(self.dictionary[self.nexttoken])
