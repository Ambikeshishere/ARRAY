# average of 3 numbers 

def calc_avg(a,b,c):
    s = a + b +c
    output = s/3
    print(output)
    return output


a = input("Enter your first number \n")
b = input("Enter your second number \n")
c = input("Enter your third number \n")
a = float(a)
b = float(b)
c = float(c)

calc_avg(a,b,c)