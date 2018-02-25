from sympy import factorint


def R(k):
    sum = 1
    for i in range(1,k):
        sum += 10**(i)
    return sum


factors = set()

k = 1
while len(factors) < 40:
    if k%5 == 0 or k%2 == 0:
        for factor in factorint(R(k)).keys():
            factors.add(factor)
    k+=1

print(factors)
print(sum(factors))
