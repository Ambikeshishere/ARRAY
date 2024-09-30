'''
Given an array of integers(nums) and an integer(target) return, 
indicies of the two numbers such that they add up to (target)
'''
class Solution:
    def twoSum(nums,target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return[i,j]
                print([i,j])
        return
    
print(Solution.twoSum([4,2,5,6],11))