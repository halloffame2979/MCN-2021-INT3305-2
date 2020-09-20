import math
import numpy as np

def prob(n, p):
    #p * (1-p)^(n-1)
    return p * (1-p)**(n-1)

def infoMeasure(n, p):
    P = prob(n, p)
    return -P*math.log2(P)

def sumProb(N, p):
    sum = float(0)
    for i in range(N):
        sum += prob(i+1, p)   
    return sum
print("sum = ",sumProb(10, 1/2))
""" 
    p(k) = p * (1-p)**(k-1)
    sumProb = 1 - (1-p)**N
    N to inf, sumProb to 1
"""

def approxEntropy(N, p):
    sum = float(0)
    for i in range(N):
        sum+= infoMeasure(i+1, p)

    return sum

print(approxEntropy(1074,0.5))
"""
    approxEntropy(N, p) is sum of all I(k,p) with k from 1 to inf
"""






