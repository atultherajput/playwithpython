#Finding Prime Numbers using Sieve of Eratosthenes Algorithm
import time
import math
def primes_sieve(n):
    m = n+1
    numbers = [True for i in range(m)]
    for i in range(2, int(math.sqrt(n))):
        if numbers[i]:
            for j in range(i*i, m, i):
                numbers[j] = False
    primes = []
    for i in range(2, m):
        if numbers[i]:
            primes.append(i)
    return primes
start = time.time()
#a=primes_sieve(10**6)
print (primes_sieve(10**6))
print (time.time() - start)
