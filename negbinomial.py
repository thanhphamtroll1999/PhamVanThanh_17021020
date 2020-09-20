import math

def prob(n,p,r):
    return (math.factorial(n)/(math.factorial(n-r+1)*math.factorial(r-1))) * pow(p,n)


def infoMeasure(n,p,r):
    return -math.log2(prob(n,p,r))


def sumProb(N,p,r):
    sum=0
    for x in range(1,N+1):
        sum+=prob(x,p,r)
    return sum


def approxEntropy(N,p,r):
    sum=0
    for x in range(1,N+1):
        sum+=infoMeasure(x,p,r)
    return (sum/N)