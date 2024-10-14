# Generate Parentheses

'''
Given n pairs of parentheses, write a function
to genrate all combinations of well - formed
parantheses
'''


class Ambikesh:
    def genParen(n):
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
            
        
        result = []
        backtrack()
        return result

m = 3
print(Ambikesh.genParen(m))