from random import randint
from math import log,floor

def gen_digits(N): # generate sequence of random digits
    i = 0
    while i < N:
        yield randint(0,9)
        i+=1

def pprint(iterable):
    for i in iterable:
        print(i)

def count_runs(sq,c = 3): # takes iterable of integers, optional digit to match against
    runs = []

    i = 0
    k = 0
    for dig in sq:
        if dig == c and k == 0:
            k = 1
            runs.append((i-k+1,k))
        elif dig == c and k != 0:
            k += 1    
            runs.append((i-k+1,k))
        elif dig != c and k != 0:
            k = 0
        i+=1

    run_counts = [[0 for i in range(11)] for i in range(10)]
    for pos,length in runs:
        if pos == 0: # need to catch this case to avoid log(0) erroring out
            run_counts[0][length-1] += 1
        else:
            run_counts[floor(log(pos,10))][length-1] += 1
    return run_counts


N = 10**6
pi_data = {}
rand_data = {}
e_data = {}

with open("/Users/Mike/Dropbox/TU-17-18/spsolving/HW2/pi_3/pi-billion.txt", 'r') as f:
    pi = f.read()
with open('e.txt','r') as f:
    e = f.read()

e = e.replace('\n','')
e = list(e)
e = list(map(int,e[:N+1]))

pi = list(pi)
del pi[1] # remove '.'
pi = list(map(int,pi[:N+1]))

rand_data['run_counts'] = count_runs(gen_digits(N))
pi_data['run_counts'] = count_runs(pi[0:N])
e_data['run_counts'] = count_runs(e[0:N])

pprint(rand_data['run_counts'])
pprint(e_data['run_counts'])
pprint(pi_data['run_counts'])
