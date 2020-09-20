import math
from math import comb
import numpy as np




def prob(n, p, N):
    #p * (1-p)^(n-1)
    return comb(N,n)*p**n*(1-p)**(N-n)

def infoMeasure(n, p, N):
    P = prob(n, p, N)
    return -P*math.log2(P)

def sumProb(p, N):
    sum = float(0)
    for i in range(N+1):
        sum += prob(i, p, N)  
    return sum
print("sum = ",sumProb(1/2,1))


def approxEntropy(p, N):
    sum = float(0)
    for i in range(N+1):
        sum+= infoMeasure(i, p, N)

    return sum

print(approxEntropy(1/2,4))







