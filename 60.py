# Multiple Inheritence

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to Class B"

class C(A,B):
    varC = "Welcome to class C"

C1 = C()

print(C1.varA)
print(C1.varB)
print(C1.varC)