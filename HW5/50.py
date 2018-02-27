from sympy import primerange, isprime
import time

N = 10**6 # our upper limit
rnge = 1,N//200 # just a heuristic, could probably come up with a programatic estimate using distribution of primes

primes = list(primerange(*rnge)) # all primes in range

# generate all primes that are sums of primes in our range
# not very pretty or efficient, but fast enough
sums = [(j-i,sum(primes[i:j])) for i in range(*rnge) for j in range(*rnge)
        if i<j and j <= len(primes) and isprime(sum(primes[i:j])) and sum(primes[i:j]) < N]

lengths, sums = zip(*sums) # unzip tuples
ind = lengths.index(max(lengths)) # get index of max sum 

print(sums[ind]) # max sum
