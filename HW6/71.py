# Do a binary search over the Farey sequence
# Stopping condition given by denom > 10e6

ln = 0 # left numerator
ld = 1 # left denominator
rn = 1 # right numerator
rd = 1 # right denominiator 

while ld + rd < 1000000:
    
    mn = ln + rn # middle numerator
    md = ld + rd # middle denominator

    if (7*mn > 3*md) or (mn == 3 and md == 7): # if middle >= 3/7
        rn = mn # assign right to middle
        rd = md
    else: # if middle < 3/7
        ln = mn # assign left to middle
        ld = md  

print(mn)
