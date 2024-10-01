'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.'''

class Solution:
    def isValid( s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack
    
x = input("Give a string containing just the characters '(', ')', '{', '}', '[' and ']' \n")
print(Solution.isValid(x))



