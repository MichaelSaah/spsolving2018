import pickle
import matplotlib.pyplot as plt
from math import floor

with open('all_tups','rb') as f:
    all_tups = pickle.load(f)

#x,y = zip(*all_tups)

x = []
y = []
c = []
colors = {1:'c' , 2: 'b' , 3: 'g' , 4: 'y', 5:'k', 6: 'r', 7: 'm'}
tup_lengths = [i for i in range(1,8)]



for k in tup_lengths:
    for i in range(1,7):
        #tup_counts = [0 for i in range(7)]
        tup_count = 0
        for tup in all_tups:
            if tup[0] < 10**i and tup[1] == k:
                #tup_counts[tup[1]-1] += 1
                tup_count += 1
        #x += [i for j in range(7)]
        #y += tup_counts
        x.append(10**i)
        y.append((tup_count - floor(10**(i-k)))/10**i)
        c.append(colors[k])

print(x)
print(y)

fig = plt.figure()
ax = plt.gca()
ax.scatter(x,y,c=c)
ax.set_xscale('log')
#ax.set_yscale('log')

plt.show()
