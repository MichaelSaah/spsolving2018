import pickle
import pprint
pp = pprint.PrettyPrinter()
import matplotlib.pyplot as plt

with open('data_sorted','rb') as f:
    data_sorted = pickle.load(f)

primes = []
reln = []
tickMap = {} # need for adding labels to scatter plot

for i,key in enumerate(data_sorted.keys()):
    for (p,q) in data_sorted[key]:
        primes.append(p)
        reln.append(i)
        tickMap[i] = key
print(tickMap)
        
def tickFunc(x,pos):
    if x%1 == 0 and 0<=x<=(len(tickMap)-1):
        return tickMap[x]
    else:
        return ''


fig, ax = plt.subplots()
ax.scatter(reln,primes,s = 4, alpha = 0.5)
ax.xaxis.set_major_formatter(plt.FuncFormatter(tickFunc))
ax.set_xlabel('Relation')
ax.set_ylabel('Prime')
ax.set_title('Density of Primes by Period Relationship')

plt.show()
