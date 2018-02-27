from collections import deque
from sympy import factorint

def check_for_match(window, desired_length):
    
    window = list(map(factorint, window)) # factor each integer
    
    window = [len(d.keys()) for d in window] # get number of unique factors for each integer
    
    window = list(map(lambda x: x==desired_length, window)) # check to see if each meets our condition
    
    return all(window) # return true if all integers meet condition

desired_length = 4

# this deque will pop the 0th element when a new one is pushed to the end, like a sliding window
window = deque([644, 645, 646, 647], maxlen=desired_length) 

i = 648 # start here, since we're given that this is where the first 3-set occurs

while True:
    if check_for_match(window, desired_length):
        print(window[0])
        break
    else:
        i += 1
        window.append(i)


