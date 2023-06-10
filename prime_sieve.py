from math import *
import time
n = 100000

v = [True for _ in range(0,n+1)]
for i in range(0,2):
    v[i]=False


def eratosthenes(num):
    
    for i in range(2,int(sqrt(num))+1):
        if v[i]:
            for j in range(i*i,num+1,i):
                v[j]=False
        
prime=[]

def euler(n):
    sieve = list(range(2, n + 1))
    i = -1
    k = -1
    while k:
        k = 0
        i += 1
        while (factor := sieve[i + k] * sieve[i]) <= n:
            sieve.remove(factor)
            while (factor := factor * sieve[i]) <= n:
                sieve.remove(factor)
            k += 1
    return sieve
         



        

def euler2(num):
    for i in range(2,num//2+1):
        if v[i]:
            
            prime.append(i)
            
        for j in prime:
            tmp=j*i
            if tmp >= n+1:
                break
            v[tmp]=False
            if i%j==0:
                break     
res=[]
start = time.time()
euler2(n)
end = time.time()
print(end-start)

for i in range(n+1):
        if v[i]:
            res+=[i]
print(len(res))

res=[]
start = time.time()
eratosthenes(n)
end = time.time()
print(end-start)

for i in range(n+1):
        if v[i]:
            res+=[i]
   
print(len(res))
