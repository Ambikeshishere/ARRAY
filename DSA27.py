# 4 Sum

'''
Given an Array nums if n integers return an array of all the uniques quadriplets [ nums[a], nums[b], nums[c], nums[d]], such that 
nums[a] + nums[b] + nums[c] + nums[d] = target
'''

class Ambikesh:
    def fourSum( nums, target):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left , right = j + 1 , n - 1
                while left < right:
                    total = nums[i] + nums [j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j],nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right  and nums[right] == nums[right -1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

x = [1,0,-1,0,-2,2]
t = 0

v = Ambikesh.fourSum(x,t)
print(v)