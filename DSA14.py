'''
You are climbing staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many ways distinct ways can you climb to the top?
'''
class Ambikesh:
    def seedhi(s):
        if s == 1:
            return 1
        if s == 2:
            return 2
        
        D = [0] * (s+1)
        D[1] = 1
        D[2] = 2
        
        for i in range(3, s+1):
            D[i] = D[i-1] + D[i-2]
        
        return D[s]
    
n = input("Seedhi chadne ke liye kul step kitne hai \n")
n = int(n)

print(Ambikesh.seedhi(n))