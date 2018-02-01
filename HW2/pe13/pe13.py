numbers = []
with open('numbers','r') as f:
    for line in f:
        numbers.append([int(x) for x in str(line).replace('\n','')])

sums = [0 for i in range(50)] # index i corresponds to 0-9 * 10^i in sum

for i in range(50):
    for d in numbers:
        sums[i] += d[i]

sums.reverse()

for i in range(len(sums)):
    while(sums[i])>9:
        for k in reversed(range(1,4)):
            rem = sums[i]%(10**k)
            try:
                sums[i+k] += (sums[i]-rem)/(10**k)
            except IndexError:
                sums.append(0)
                sums[i+k] += (sums[i]-rem)/(10**k)                
            sums[i] = rem

sums = list(map(int,sums))

while sums[-1] == 0:
    del sums[-1]    

first_ten = ''
sums.reverse()
for i in range(10):
    first_ten += str(sums[i])

print(first_ten)
    
