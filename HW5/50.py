from sympy import primerange, isprime
import time

start = time.time()

N = 10**6
rnge = 1,N//200 # just a heuristic, could probably come up with a programatic estimate using distribution of primes
primes = list(primerange(*rnge))

sums = [(j-i,sum(primes[i:j])) for i in range(*rnge) for j in range(*rnge)
        if i<j and j <= len(primes) and isprime(sum(primes[i:j])) and sum(primes[i:j]) < N]

lengths, sums = zip(*sums)
ind = lengths.index(max(lengths))

print(sums[ind], lengths[ind])
print(time.time() - start)
