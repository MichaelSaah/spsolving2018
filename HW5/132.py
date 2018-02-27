from sympy import sieve

num_facs = 40
N = 10**9

factors = []

for prime in sieve:
    if pow(10, N, 9*prime) == 1:
        factors.append(prime)
        
        if len(factors) == 40:
            break

print(sum(factors))
