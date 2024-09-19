# WAP to check if a list contains a palindrome of elements.
#palindrome ka matlab hai jisko reverse karne pe bhi wahi value mile jo pahle thi 
list1 = [1,2,5,2,1]
list2 = [4,5,8,3,6]

list3 = list1.copy()
list3.reverse()
print("List1 is :- ",list1)
print("List2 is :- ",list2)

list4 = list2.copy()
list4.reverse()

if (list1 == list3):
    print("List 1 is palindrome")
else:
    print("List1 is not a palindrome")


if (list2 == list4):
    print("List 2 is palindrome")
else:
    print("List2 is not a palindrome")