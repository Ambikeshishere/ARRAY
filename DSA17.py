'''
Give a string s, return the longest palindromic substring s.
'''

def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return " "
    
    longest = s[0]
    for i in range(n):
        for j in range(i+1,n+1):
            if is_palindrome(s[i:j]) and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest


s = input("Enter the palindromic strings \n")
print(longest_palindrome(s))