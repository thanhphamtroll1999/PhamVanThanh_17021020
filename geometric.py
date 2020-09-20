import math

def prob(n,p):
    return pow(p,n)


def infoMeasure(n,p):
    return -math.log2(pow(p,n))


def sumProb(N,p):
    sum=0
    for x in range(1,N+1):
        sum+=pow(p,x)
        '''
        sum(1)=1/2
        sum(2)=1/2+1/4
        sum(3)=1/2+1/4+1/8
        vế phải là 1 cấp số nhân lùi vô hạn => sum(N)=1

        '''
    return sum


def approxEntropy(N,p):
    sum=0
    for x in range(1,N+1):
        sum+=-math.log2(pow(p,x))
    return (sum/N)
'''
   log2(p,x)=x*log2(p)=x;
   đầu ra sẽ bằng (1+2+3+4+...+N)/N
   mà entropy của phân phối geometric là
   (1+2+3+...+N)/(2+4+8+...+2^N)
'''




