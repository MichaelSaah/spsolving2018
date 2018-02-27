from sympy import sieve

num_facs = 40 # the number of prime factors we are looking for
N = 10**9 # the size of the repunit we want to factor

factors = []

"""
The trick here is to realize that R(k) can be written as 

R(k) = (10^k - 1)/9

which can be interpreted as shifting .111111... up k places and then
throwing away the decimal.

Thus if we want to know that R(k) mod p = 0, we can check that

(10^k - 1)/9 mod p = 0
<=>
(10^k - 1) mod 9p = 0
<=>
10^k mod 9p = 1

In our code, we use the fact that python's pow() has an optimized
mod routine for integer values.

"""

for prime in sieve:
    if pow(10, N, 9*prime) == 1:
        factors.append(prime)
        
        if len(factors) == 40:
            break

print(sum(factors))
