import pickle

with open('data','rb') as file:
    data = pickle.load(file)

# recognized relationships between prime and period, q = f(p)
data_sorted = {'2p + 2':[], '1p - 1':[], '(2/3)p + (2/3)':[], '(1/2)p - (1/2)':[], '(1/3)p - (1/3)':[], '(2/7)p + (2/7)':[], 'unknown':[]}

# sort tuples into dict by rel'n type
for (p,q) in data:
    if q == 2*p+2:
        data_sorted['2p + 2'].append((p,q))
    elif q == p-1:
        data_sorted['1p - 1'].append((p,q))
    elif q == 0.5*(p-1):
        data_sorted['(1/2)p - (1/2)'].append((p,q))
    elif q == (2*p+2)/3:
        data_sorted['(2/3)p + (2/3)'].append((p,q))
    elif q == (p-1)/3:
        data_sorted['(1/3)p - (1/3)'].append((p,q))
    elif q == (2*p+2)/7:
        data_sorted['(2/7)p + (2/7)'].append((p,q))
    else:
        data_sorted['unknown'].append((p,q))

with open('data_sorted','wb') as file:
    pickle.dump(data_sorted,file)


