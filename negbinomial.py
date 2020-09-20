import math
from math import comb
import numpy as np




def prob(n, p, r):
    #p * (1-p)^(n-1)
    return comb(n+r-1, n)*p**r*(1-p)**n

def infoMeasure(n, p, r):
    P = prob(n, p, r)
    return -P*math.log2(P)

def sumProb(p, r, N):
    sum = float(0)
    for i in range(N):
        sum += prob(i, p, r)  
        print("prop{} = {}".format(i, prob(i+1, p, r))) 
    return sum
print("sum = ",sumProb(1/2,10,100))


def approxEntropy(p, r, N):
    sum = float(0)
    for i in range(N):
        sum+= infoMeasure(i, p, r)

    return sum

print(approxEntropy(1/2,10,100))







