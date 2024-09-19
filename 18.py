# WAP to Find the greatest of 3 numbers entered by the user.

num1 = input("Chalo pahla number batao \n")
num2 =input("Ab dusra wala batao\n")
num3 =input("Ab teesra wala batao\n")
if (num1 > num2 and num2 > num3):
    print("Pahla wala sabse bada number hai\n")
elif(num2 > num1 and num1 > num3):
    print("Dusra wala sabse bada number hai\n")
else:
    print("Teesra wala sabse bada number hai\n")