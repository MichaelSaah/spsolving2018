layers = 501
rh_corners = [2*i+1 for i in range(1,layers)]
diff = [2*(i+1) for i in range(layers)]

sum = 1 # start with center element

for x,d in zip(rh_corners,diff):
    for i in range(4):
        sum += x**2 - i*d

print(sum)
