import pickle
import matplotlib.pyplot as plt

with open('all_tups','rb') as f:
    all_tups = pickle.load(f)

#x,y = zip(*all_tups)

x = []
y = []
stops = [10**k for k in range(1,7)]

for i in stops:
    #tup_counts = [0 for i in range(7)]
    tup_count = 0
    for tup in all_tups:
        if tup[0] < i and tup[1] == 3:
            #tup_counts[tup[1]-1] += 1
            tup_count += 1
    #x += [i for j in range(7)]
    #y += tup_counts
    x.append(i)
    y.append(tup_count)


print(x)
print(y)

fig = plt.figure()
ax = plt.gca()
ax.scatter(x,y)
#ax.set_yscale('log')
ax.set_xscale('log')

plt.show()
