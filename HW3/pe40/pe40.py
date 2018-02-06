digits = []

i = 1
while len(digits) < 10**6:
    digits += list(map(int,list(str(i))))
    i+=1

prod = 1

for k in range(6):
    prod *= digits[10**k - 1]

print(prod)
