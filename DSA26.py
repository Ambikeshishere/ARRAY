# Letter Combination of a phone number 

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could reperesent. Return the answer in any order.
'''

class Ambikesh:
    def Combination(digits):
        if not digits:
            return[]
        
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        result = []

        def back(index, path):
            if index == len(digits):
                result.append(path)
                return
            for letter in mapping[digits[index]]:
                back(index+1 ,  path  + letter)
        
        back(0,"")
        return result
    
x = input("Enter the valur of digits that you want to convert in to alphabets \n")
y = Ambikesh.Combination(x)
print(y)