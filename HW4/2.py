from sympy.ntheory.generate import prime
import matplotlib.pyplot as plt

def prime_difference(N):
    primes_1 = 0
    primes_3 = 0
    diff = [] # primes_1 - primes_3 at prime i
    for i in range(1,N): # prime() starts at 1
        p = prime(i)%4
        if p == 1:
            primes_1 += 1
        elif p == 3:
            primes_3 += 1
        diff.append(primes_1 - primes_3)
    
    return diff

N = 1000

plt.plot(prime_difference(N))
plt.title('|Primes congr 1 mod 4| - |Primes congr 3 mod 4|')
plt.show()
