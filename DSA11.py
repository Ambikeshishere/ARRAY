# plus one 

class Ambikesh:
    def plus_one(digit):
        n = len(digit)
        for i in range(n-1,-1,-1):
            if digit[i] < 9:
                digit[i] += 1
                return digit
            digit[i] = 0
        return[1] + digit
digit = [1,2,3]
x = Ambikesh.plus_one(digit)
print(x)