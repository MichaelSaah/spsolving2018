from math import factorial as fac
import time

def dig_fac(x):
    x = list(map(int,list(str(x))))
    x = list(map(fac,x))
    return sum(x)

def good_keys(d):
    v=list(d.values())
    k=list(d.keys())
    v_i = [i for i,x in enumerate(v) if x == 60]
    ret = len([k[i] for i in v_i])
    return ret


start_time = time.time()

N = 10**6
chains = {}

for i in range(N):
    seen = [i]
    next = i
    while True:
        next = dig_fac(next)
        if next in chains.keys():
            chains[i] = len(seen) + chains[next]
            break
        elif next in seen:
            chains[i] = len(seen)
            break
        else:
            seen.append(next)

print(good_keys(chains))
print(time.time()-start_time)        


