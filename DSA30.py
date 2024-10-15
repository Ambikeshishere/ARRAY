# Search in Rotated Sorted Array

'''
There is an Integer array nums sorted in ascending order (with distinct values).

Given the array nums after possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.
'''

class Ambikesh:
    def Search (nums, target):
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums [mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(Ambikesh.Search(nums, target))