from math import factorial as fac
import time

def dig_fac(x): # return sum of factorial of digits
    x = list(map(int,list(str(x))))
    x = list(map(fac,x))
    return sum(x)

def num_good_keys(d, target): # return number of matching values in our dictionary
    v = list(d.values())
    v = [x for x in v if x == target]
    return len(v)


N = 10**6 # upper limit
target = 60 # desired chain lenght
chains = {} # this dict will map an integer to the length of its non-repeating chain

for i in range(N): # for each i up to N
    seen = [i] # keep track of where we've been
    next = i
    while True:
        next = dig_fac(next) # get next term in chain

        if next in chains.keys(): # if we know the length of next's chain, then
            chains[i] = len(seen) + chains[next] # add that to seen to get chain length for i
            break

        elif next in seen: # if we end up where we've been, then
            chains[i] = len(seen) # we've found the end of the chain
            break

        else:
            seen.append(next)

print(num_good_keys(chains, target)) # print number of integers that have a chain of length 60


