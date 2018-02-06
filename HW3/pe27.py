import sympy

isPrime = sympy.ntheory.primetest.isprime

A = range(-999,1000)
B = range(-1000,1001)

coeffs = [(a,b) for a in A for b in B]
#coeffs = [(1,41),(-79,1601)] # test coeffs

longest = 0
best_coeffs = (None,None)

def quad(a,b,x):
    return x**2 + a*x + b

for (a,b) in coeffs:
    i = 0
    while isPrime(quad(a,b,i)):
        i += 1
    if i > longest:
        longest = i
        best_coeffs = (a,b)

print(best_coeffs[0]*best_coeffs[1])
