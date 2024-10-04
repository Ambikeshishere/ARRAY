'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

class Ambikesh:
    def LengthofSubstring(s):
        char = set()
        left = 0
        length = 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1
            char.add(s[right])
            length = max(length,right - left + 1)
        return length
    


s = input("Enter the string \n")    
print(Ambikesh.LengthofSubstring(s))
