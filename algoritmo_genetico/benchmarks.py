import math
import random as rnd

def rosenbrock(a):
    sigma = 0
    for i in range(len(a) - 1):        
        sigma += (1 - a[i])**2 + 100 * (a[i+1] - a[i]**2)**2
    
    return(sigma)


def rastringin(a):
    sigma = 0
    for i in a:
        sigma += i**2 - 10 * math.cos(2 * math.pi * i)

    res = 10 * len(a) + sigma
    return(res)


def schaffer(a):
    sigma = 0
    for i in range(len(a)-1):
        x = a[i]**2 + a[i+1]**2
        corchete = math.sin(50 * x**0.10)** 2 + 1
        
        sigma += x**0.25 * corchete
        
    return(sigma)


def ellipsoid(a):
    sumi = 0
    for i in range(len(a)):
        sumj = 0
        for j in range(i):
            sumj += a[j]**2
        sumi += sumj        
    
    return(sumi)
    

def trid(a): 
    suml = (a[0] - 1)**2
    sumr = 0
    for i in range(1, len(a)):
        suml += (a[i] - 1)**2
        sumr += (a[i] - (a[i-1]))
    
    res = suml - sumr
    return(res)


def brown(a):    
    sigma = 0
    for i in range(len(a) - 1):
        x = (a[i]**2)**(a[i+1]**2 + 1)
        y = (a[i+1]**2)**(a[i]**2 + 1)
        sigma += x + y

    return(sigma)


def salomon(a):
    sigma = 0
    for i in a:
        sigma += i**2
    
    sigma = sigma ** 0.5
    res = 1 - math.cos(2 * math.pi * sigma) + 0.1 * sigma
    return(res)


def tank(a):
    sigma = 0
    for i in a:
        sigma += i**4 - 16*(i**2) + 5*i
    
    sigma *= 0.5
    
    return sigma

def quartic(a):
    sigma = 0
    for i in range(len(a)):
        sigma += i * a[i]**4 + rnd.random()

    return(sigma)

# a = [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0]
# print(len(a))
# print(sum(a))
# ellipsoid(a)
# schaffer(a)
# trid(a)
# brown(a)
# rosenbrock(a)
# salomon(a)
# rastringin(a)