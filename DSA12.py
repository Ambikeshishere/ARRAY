# Given two binary strings a and b, return their sum as a binary string.

class Ambikesh:
    def binary_sum(a,b):
        i = max(len(a), len(b))
        a = a.zfill(i)
        b = b.zfill(i)
        op = ''
        carry = 0
        for i in range(i-1,-1,-1):
            sum = carry
            sum += 1 if a[i] == '1' else 0
            sum += 1 if b[i] == '1' else 0
            op = ('1' if sum % 2 == 1 else '0') + op
            carry = 0 if sum < 2 else 1
        if carry != 0:
            op = '1' + op
        return op.zfill(i)
    
a = input("Enter the value of first binary number \n")
b = input("Enter the value of second binary number \n")
print("Your sum is :- " , Ambikesh.binary_sum(a,b))