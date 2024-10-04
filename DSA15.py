'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.
'''


class Solution:
    def merge( nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idxm = m-1
        idxn = n-1

        gt = m+n-1

        while idxn >= 0:
            if idxm >= 0 and nums1[idxm] > nums2[idxn]:
                nums1[gt] = nums1[idxm]
                idxm -= 1
            else:
                nums1[gt] = nums2[idxn]
                idxn -= 1
            
            gt -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5,6]
n = 3
Solution.merge(nums1, m, nums2, n)
print(nums1) 
