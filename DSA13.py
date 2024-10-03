# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

class Ambikesh:
    def sqrt(x):
        if x == 0:
            return 0
        
        L = 1
        R = x
        while L <= R :
            M = (L + R) // 2
            if M * M == x:
                return M
            elif M * M < x:
                L = M + 1
            else:
                R = M - 1
        return R
x = input("Enter the value of x :- \n")
x = int(x)
print(Ambikesh.sqrt(x))