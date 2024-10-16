
# Find First and last position of element in sorted array.

'''
Given an array of integers nums are sorted in non-decreasing order,
find the starting and ending position of a given target value.
'''


class Ambikesh:
    def searchRange( nums, target) :
        
        def B_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = B_search(nums, target, True)
        right = B_search(nums, target, False)
        
        return [left, right]


nums = [5,7,7,8,8,10]
target = 8
print(Ambikesh.searchRange(nums, target))