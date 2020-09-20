import math

def prob(n,p,N):
    return (math.factorial(N)/(math.factorial(n)*math.factorial(N-n))) * pow(p,N)


def infoMeasure(n,p,N):
    return -math.log2(prob(n,p,N))


def sumProb(N,p):
    sum=0
    for x in range(1,N+1):
        sum+=prob(x,p,N)
        '''
        sum(1)=C 1 của N nhân với 1/2
        sum(2)=sum(1)+C 2 của N nhân với 1/4
        
        '''
    return sum

def approxEntropy(N,p):
    sum=0
    for x in range(1,N+1):
        sum+=infoMeasure(x,p,N)
    return (sum/N)
                   
