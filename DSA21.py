'''
Given an input string s and a pattern p, implement 
regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
'''

class Solution:
    def isMatch(s,p):
        memo = {}
        def dp(i,j):
            if(i,j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = (dp(i,j+2) or first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1,j+1)
                memo[i,j] = ans
            return memo [i,j]
        return dp(0,0)

s = input("Enter the string \n")
p = input("Enter the pattern \n")

x = Solution.isMatch(s,p)
print(x)