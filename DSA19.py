'''
Given a 32 bit integer x returnx with its digits reversed,
if reversing x cause the value to go 
outside the signed 32 bit integer range [-2^31,2^31,-1]
then return 0.
'''



class Ambikesh:
    def rv(x):
        s = -1 if  x < 0 else 1
        x *= s
        rev_x = int(str(x)[::-1])
        if rev_x > 2**31 - 1:
            return 0
        return s*rev_x
    
c = input("Enter the 32 bit number\n")
c = int(c)
num = Ambikesh.rv(c)

print(num)