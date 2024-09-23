# WAF to find the factorial of n. (n is the parameter)

n = input("Enter your number")
n = int(n)
def factorial(number):
    k = 1
    for i in range(1, n+1):
        k *= i
    print(k)
    
factorial(n)