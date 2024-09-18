#find maximum of two numbers 

a = input("Enter your first number- ")
b = input("Enter your second number- ")

a = float(a)
b = float(b)

print(type(a))
print(type(b))

if (a > b):
    print(a," is greater than ", b)
else:
    print(b,"is greater than ",a)