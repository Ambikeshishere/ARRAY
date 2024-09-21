# Search for a numer x in this tuple using loop.

tup = (1,4,9,16,25,36,49,64,81,100)

x = 49
idx = 0
for val in tup:
    if (val == x):
        print("found at", idx)
        break
    else:
        print("not Found")
    idx +=1