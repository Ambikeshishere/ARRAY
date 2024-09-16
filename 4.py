#Remove Duplicates from Sorted Arrays

class solution :
    nums = input("Enter your number \n ")
    def removeDuplicates(a, nums: list[int]) -> int:
        j = 1
        for i in range(1 , len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j = j+1
        return j