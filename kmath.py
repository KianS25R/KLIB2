"""math script by kian"""

def pi() -> float:
    """returns first 100 digets of pi"""
    return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

def sqrt(number) -> float:
    """returns squareroot of number"""
    return number**(1/2)

def nrt(base: float, n: float) -> float:
    """returns root-n for the base"""
    return base**(1/n)

def asin(number: float) -> float:
    """returns inverse sinus for number"""
    return number+((number**3)/6)+((3*number**5)/40)+((5*number**7)/112)+((35*number**9)/1152)+((63*number**11)/2816)+((231*number**13)/13312)

def acos(number: float) -> float:
    """returns inverse cosin for number"""
    return (pi()/2)-asin(number)

def acosdeg(number: float) -> float:
    """acos but degress instead of radians"""
    return deg(acos(number))

def asindeg(number: float) -> float:
    """asin but returns degress instead of radians"""
    return deg(asin(number))

def deg(radians: float) -> float:
    """turns radians into degress"""
    return radians*(180/pi())

def atan(number: float) -> float:
    """returns inverse tan for number"""
    if abs(number) <= 1:
        return number-((number**3)/3)+((number**5)/5)-((number**7)/7)+((number**9)/9)
    elif number > 1:
        return pi()/2 - atan(1/number)
    else:
        return -(pi()/2) - atan(1/number)
    
def atan2(y: float, x: float) -> float:
    """returns atan2 for y, x"""
    if x > 0:
        return atan(y / x)
    elif x < 0 and y >= 0:
        return atan(y / x) + pi()
    elif x < 0 and y < 0:
        return atan(y / x) - pi()
    elif x == 0 and y > 0:
        return pi() / 2
    elif x == 0 and y < 0:
        return -pi() / 2
    elif x < 0 and y == 0:
        return pi()
    else:
        return 0

def sin(opp: float, hypo: float) -> float:
    """returns sinus to opp/hypo"""
    return opp/hypo

def cos(adja: float, hypo: float) -> float:
    """returns cosin to adja/hypo"""
    return adja/hypo

def tan(opp:float, adj:float) -> float:
    """returns tan to opp/adj"""
    return opp/adj



def factorial(n) -> float:
    base = 1
    for i in range(1, n + 1):
        base *= i
    return base

def exp(x, terms=20) -> float:
    total = 1
    term = 1

    for n in range(1, terms):
        term *= x / n
        total += term

    return total

def log(x: float, terms=20) -> float:
    if x <= 0:
        raise ValueError("x must be > 0")
    y = x - 1
    total = 0
    for n in range(1, terms + 1):
        term = (y ** n) / n
        if n % 2 == 1:
            total += term
        else:
            total -= term
    return total

def sinh(x: float) -> float:
    return (exp(x)-exp(-x))/2

def cosh(x: float) -> float:
    return (exp(x)+exp(-x))/2

def maximum(x: float) -> float:
    if x > 0:
        return x
    else:
        return 0

def tanh(x: float) -> float:
    return sinh(x)/cosh(x)

def coth(x: float) -> float:
    return cosh(x)/sinh(x)

def sech(x: float) -> float:
    return 1/cosh(x)

def csch(x: float) -> float:
    return 1/sinh(x)

def arsinh(x: float) -> float:
    return log(x+sqrt((x**2)+1))

def sigmoid(x: float) -> float:
    return 1/(1+exp(-x))

def ReLu(x: float) -> float:
    if x <=0:
        return 0
    else:
        return x
    
def ELU(x: float, alpha: float = 1.0) -> float:
    if x > 0:
        return x
    else:
        return alpha*(exp(x)-1)
    
def LeakyReLu(x: float, leak: float = 0.01) -> float:
    if x > 0:
        return x
    else:
        return leak*x

def Epsilon() -> float:
    return 10**(-8)

def FixSoftmax(x: list) -> list:
    newlist = []
    d = 0
    for i in x:
        d += exp(i-max(x))
    for i in x:
        newlist.append((exp(i-max(x)))/d)
    return newlist

def softplus(x: float) -> float:
    return log(1+exp(x))