import pickle
import matplotlib.pyplot as plt
from math import floor

with open('all_tups','rb') as f:
    all_tups = pickle.load(f)

colors = {1:'c' , 2: 'b' , 3: 'g' , 4: 'y', 5:'k', 6: 'r', 7: 'm'}
max_N_log = 4
fig = plt.figure()
ax = plt.gca()

# cut all_tups down to size
#for i,tup in enumerate(all_tups):
#    if tup[0] > 10**max_N_log:
#        all_tups = all_tups[0:i]
#        break

for k in range(1,6): # tup lengths
    x = []
    y = []
    for i in range(1,7): # range
        tup_count = 0
        for tup in all_tups:
            if tup[0] < 10**i and tup[1] == k:
                tup_count += 1
        x.append(10**i)
#        y.append(abs((tup_count - floor(10**(i-k)))/max(1,floor(10**(i-k)))))
#        y.append(tup_count)
        y.append(floor(10**(i-k)))
    print(y)
    ax.scatter(x,y,c=colors[k],label = str(k))

ax.set_xscale('log')
ax.set_xlabel('Digits Checked')
ax.set_ylabel("Number of Strings of 3's")
ax.legend( )

plt.show()
