#find minimum of two numbers 

a = input("Enter your first number- ")
b = input("Enter your second number- ")

a = float(a)
b = float(b)

print(type(a))
print(type(b))

if (a < b):
    print(a," is lesser than ", b)
else:
    print(b,"is lesser than ",a)