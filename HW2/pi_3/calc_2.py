import pickle

with open('pi-billion.txt','r') as f:
    pi = f.read()

all_tups = []

i=0

while i < 4000000:
    if pi[i] == '3':
        k = 0
        while pi[i+k] == '3':
            k += 1
            all_tups.append((i+k,k))
            if 89000 < i < 89100:
                print((i+k,k))
        i += k
    else:
        i += 1
        
with open('all_tups','wb') as f:
    pickle.dump(all_tups,f)
