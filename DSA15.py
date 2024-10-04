def merge(nums1, m, nums2, n):
    # Last index of the merged array
    last = m + n - 1
    
    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    # Fill nums1 with remaining elements of nums2, if any
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 
