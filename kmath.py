"""math script by kian"""

def pi():
    return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679



def sqrt(number):
    return number**(1/2)

def nrt(base: float, n: float):
    return base**(1/n)

def asin(number: float):
    return number+((number**3)/6)+((3*number**5)/40)+((5*number**7)/112)+((35*number**9)/1152)+((63*number**11)/2816)+((231*number**13)/13312)

def acos(number: float):
    return (pi()/2)-asin(number)


def acosdeg(number: float):
    return deg(acos(number))


def asindeg(number: float):
    return deg(asin(number))

def deg(radians: float):
    return radians*(180/pi())

def atan(number: float):
    if abs(number) <= 1:
        return number-((number**3)/3)+((number**5)/5)-((number**7)/7)+((number**9)/9)
    elif number > 1:
        return pi()/2 - atan(1/number)
    else:
        return -(pi()/2) - atan(1/number)
    
def atan2(y: float, x: float):
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
