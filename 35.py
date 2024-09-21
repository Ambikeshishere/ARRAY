# Search for a number x in this tuple using loop.

x = 81

tup = (1,4,9,16,25,36,49,64,81,100)
a = len(tup)
i = 0
while i < a:
   
    if (tup[i] == x):
        print("We Got it at the index of ", i)
    else:
        print("finding......")
    i +=1 
