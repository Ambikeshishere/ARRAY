# Next Permutation

'''
A Permutation of an array of integers is an
arrangement of its member into a sequence or
linear order.
'''

class Ambikesh:
    def nextpermuattion(nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1:] = reversed(nums[i+1:])
    
x = [3, 1, 2]
Ambikesh.nextpermuattion(x)

print(x)