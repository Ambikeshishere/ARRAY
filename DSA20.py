# String to Integer (Atoi)

class Ambikesh:
    def Atoi(s):
        min , max = -2**31, 2**31-1
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sgn = 1
        if i <n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sgn = -1
            i += 1
        
        result = 0
        while i < n and s[i].isdigit():
            result = result*10 + int(s[i])
            i += 1
        result *= sgn
        if result < min:
            return min
        if result > max:
            return max
        
        
        return result

c = "123"
num = Ambikesh.Atoi(c)
print(num)