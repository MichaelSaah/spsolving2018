import matplotlib.pyplot as plt
import pickle

with open('data_sorted','rb') as f:
    data_sorted = pickle.load(f)

colorDict = {0:'b', 1:'y', 2:'g', 3:'r', 4:'m', 5:'c', 6:'grey'}

for i,key in enumerate(data_sorted.keys()):
    pp = []
    qq = []
    for (p,q) in data_sorted[key]:
        pp.append(p)
        qq.append(q)
    plt.scatter(pp,qq,c=colorDict[i],label=key,alpha=0.5)

plt.grid()
plt.legend()
plt.xlabel('Prime')
plt.ylabel('Period')
plt.title('Prime vs Period mod Prime')
plt.show()
