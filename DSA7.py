'''
REMOVE ELEMENT FROM LIST
'''


def RE(nums, val):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j


nums = [3,2,2,3]
val = 3
op = RE(nums, val)
print(f"Modified nums: {nums[:op]}")
print(f"Number of elements not equal to {val}: {op}")
