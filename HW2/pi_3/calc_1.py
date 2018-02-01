import pickle

with open('pi-billion.txt','r') as f:
    pi = f.read()

c3N = []

i=0
longest = 0

while i < 4000000:
    if pi[i] == '3':
        k = 0
        while pi[i+k] == '3':
            k += 1
        if k >= longest:
            longest = k
            c3N.append((i+k,k))
            print(i+k,k)
        i += k
    else:
        i += 1
        
with open('c3N','wb') as f:
    pickle.dump(c3N,f)
