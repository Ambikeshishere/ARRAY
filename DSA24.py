# Integer to Roman

class Ambikesh:
    def Roman(num):
        val = [
            1000,900,500,400,
            100,90,50,40,
            10,9,5,4,
            1
        ]

        syms = [
            "M","CM","D","CD",
            "C","XC","L","XL",
            "X","IX","V","IV",
            "I"
        ]

        R_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                R_num += syms[i]
                num -= val[i]
            i += 1
        return R_num

c = input("Enter the value of integer which you want to convert into roman \n")
b = int(c)
print(Ambikesh.Roman(b))