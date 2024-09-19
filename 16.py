# College Grading System

marks = input("Enter your marks - \n")
marks = float(marks)
if (marks > 90):
    print("A, Sabash beta")
elif (marks < 90 and marks >= 70):
    print("B, achaa hai")
elif (marks < 70 and marks >= 50):
    print("C, agli baar achhe se padhna")
elif (marks < 50 and marks >= 30):
    print("D, baal baal bache ho beta fail hone se")
else:
    print("FAIL ho tum budbak !")