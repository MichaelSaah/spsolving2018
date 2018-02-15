def longest_sequence(iterable, N):
    longest = [1] # longest sequence of any digits seen by a given index
    max_longest = 1 # max sequence length
    i = 1 # iterable index
    k = 1 # sequence index
    while i < N:
        if iterable[i] != iterable[i-1]:
            longest.append(longest[-1])
            k = 1
        else:
            k += 1
            if k > max_longest:
                longest.append(k)
                max_longest = k
        i+=1

    return longest

with open('/Users/Mike/Dropbox/TU-17-18/spsolving/HW2/pi_3/pi-billion.txt','r') as f:
    pi = f.read()

N = 10**3
print(pi[:N])
print(longest_sequence(pi,N))
