#SETS


sets = {1,2,3,4,5,6,"Ambikesh","Srivastava",4,45,8,3,6}
sets2 = {1,5,1,6,1,8,4,8,7,54,465,47,87,5,564,84,87}
print(sets)
print(len(sets))
null__sets = set()
print(type(sets))
print(type(null__sets))
null__sets.add(1)
null__sets.add(2)
sets.remove("Ambikesh")
#sets.clear()




print(sets)
print(null__sets)
print(null__sets.pop())
print(null__sets) 

print(sets.union(sets2))
print(sets.intersection(sets2))