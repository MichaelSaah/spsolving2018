import mpmath
import pickle

mpmath.mp.dps = 10000000

pi = str(mpmath.pi())

with open('pi','wb') as f:
    pickle.dump(pi,f)
