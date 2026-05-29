from kmath import sqrt
class vectorI():
    def __init__(self, *values):
        """creates vector with userdefined dimensions"""
        self.values = values
        self.length = len(self.values)
    def __add__(self, other):
        if type(other) == vectorI:
            if other.length == self.length:
                valuesa = []
                at = 0
                for i in self.values:
                    valuesa.append(i+other.values[at])
                    at +=1
                return vectorI(*valuesa)

    def __sub__(self, other):
          if type(other) == vectorI:
            if other.length == self.length:
                valuesa = []
                at = 0
                for i in self.values:
                    valuesa.append(i-other.values[at])
                    at += 1
                return vectorI(*valuesa)

    def __mul__(self, other):
        if type(other) == vectorI:
            if other.length == self.length:
                valuesa = []
                at = 0
                for i in self.values:
                    valuesa.append(i*other.values[at])
                    at += 1
                return vectorI(*valuesa)
        elif type(other) == float or type(other) == int:
            valuesa = []
            at = 0
            for i in self.values:
                valuesa.append(i*other)
                at += 1
            return vectorI(*valuesa)