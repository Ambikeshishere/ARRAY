''' Given an integer x, return True if x is a palindrome and false otherwise'''

class Solution:
    def isPalindrome( x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        reversed_num = 0
        original = x

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return x== reversed_num or x == reversed_num // 10
    
a = input("Enter the number which you want to test\n")
a = int(a)
print(Solution.isPalindrome(a))