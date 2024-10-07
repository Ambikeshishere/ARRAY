# Three Sum
'''
Given an Integer array nums return all the triplets [nums[i], nums[j], nums[k]]
such that i!=j , i!=k and j!=k and nums[i] + nums[j] + nums[k] == 0.
'''

class Ambikesh:
    def sum3(num):
        num.sort()
        triple = []
        n = len(num)
        for i in range(n-2):
            if i > 0 and num[i] == num[i-1]:
                continue
            left , right = i+1 , n-1
            while left < right:
                total = num[i] + num[left] + num[right]
                if total == 0:
                    triple.append([num[i], num[left], num[right]])
                    while left < right and num[left] == num[left+1]:
                        left += 1
                    while left < right and num[right] == num[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return triple
    
o = [-1,0,1,2,-1,-4]
x = Ambikesh.sum3(o)
print(x)