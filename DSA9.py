# Search Insert Position

class Ambikesh:
    def SRCs(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        return left
    
nums = input("Enter the list of number \n")
target = input("Enter the value of targeted number \n")

print(Ambikesh.SRCs(nums,target))
    