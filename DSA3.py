# Roman To Integer converter

class Solution:
    def romanToInt(s):
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for a, b in zip(s,s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]
        return res + roman[s[-1]]


x = input("Enter the Roman Number which you want to convert in number \n")
print(Solution.romanToInt(x))