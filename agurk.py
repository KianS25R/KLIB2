"""helt klar ikke en knockoff af pickle"""

def writel(*lists: list, file: str):
    """writes lists to file can be read/loaded using agurk.read(file)"""
    with open(file, "w") as f:
        towrite = ""
        for i in lists:
            a = 0
            for j in i:
                if a == 0:
                    towrite+=str(j)
                    a+=1
                else:
                    towrite+=f",{str(j)}"
            towrite += ";"
        towrite = towrite.removesuffix(";")
        f.write(towrite)


def readl(file: str) -> list:
    """returns list with lists or strings if lists were not what was saved"""
    with open(file, "r") as f:
        a = []
        data = f.read()
        splitteddata = data.split(";")
        for i in splitteddata:
            b = []
            for j in i.split(","):
                j = j.replace("[", "").replace("]", "").replace("'", "")
                b.append(j)
            a.append(b)
        return a

def write(data: list, file: str):
    """write list to file"""
    with open(file, "w") as f:
        f.write(f"a = {data}\nf=0")

def read(file: str) -> list:
    """read list from file"""
    with open(file) as f:
        data = f.read()
        f = ""
        a = {}
        exec(data,{"f": f}, a)
        return a["a"]