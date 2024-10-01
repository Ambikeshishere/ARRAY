'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.
'''

class Solution:
    def Prefix(list) :
        ans=""
        list = sorted(list)
        first = list[0]
        last = list[-1]
        for i in range(min(len(first),len(last))):
            if(first[i] != last[i]):
                return ans
            ans += first[i]
        return ans

print(Solution.Prefix(["Ambikesh","Ambani","Ambuja"]))