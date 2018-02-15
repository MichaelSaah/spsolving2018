from mpmath import li
from sympy import sieve
import matplotlib.pyplot as plt

li_offset = lambda x: li(x,offset = True)
N = 1000000
step = 1000

xx = [step*(i+1) for i in range(N//step)]
primes = list(sieve.primerange(1,N))
estimate = list(map(li_offset, xx))
actual = []
for x in xx:
    actual.append(len([prime for prime in primes if prime < x]))

yy = [a/e for a,e in zip(actual,estimate)]

plt.plot(xx,yy)
plt.title('|{primes<x}|/li(x)')
plt.show()
