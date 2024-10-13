#threeSome closet

'''
Given an Integer array nums of length n and an 
integer target' find three integers in nums that 
the sume is closet to target.
'''


class Ambikesh:
    def threeSum(nums, target):
        nums.sort()
        cl_sum = float('inf')

        for i in range (len(nums) - 2):
            left , right = i+1, len(nums)-1

            while left < right:
                cr_sum = nums[i] + nums[left] + nums[right]

                if abs (cr_sum - target) < abs (cl_sum - target):
                    cl_sum = cr_sum
                
                if cr_sum < target:
                    left += 1
                elif cr_sum > target:
                    right -= 1
                else:
                    return cr_sum
        return cl_sum

x = [-1,2,1,-4]
print(Ambikesh.threeSum(x,1))