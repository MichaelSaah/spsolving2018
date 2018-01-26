from sympy import fibonacci as fib
from sympy import sieve
import collections
import copy
import pickle

window = collections.deque([0,1,1],3) # deque object, appending to end kicks first element off the front
found = copy.copy(window) # pattern we want to check against to find period
data = []

for p in sieve.primerange(2,10000):
    q = 3 # start index counter at 3 since we're starting with the fourth fibonacci number
    while True:
        window.append(fib(q)%p)
        if window == found: # if we've looped back around
            print(p, q-3)
            data.append((p,q-3)) # add (prime,period) to list
            break
        q+=1

with open('data','wb') as file:
    pickle.dump(data,file)


