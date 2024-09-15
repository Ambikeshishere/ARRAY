#Calculator


a = input("Enter your first number : \n")
b = input("Enter your second number : \n")
c = input("Enter + - / * \n")

if c == "+" :
    sum = float(a) + float(b)
    print("The sum is : " + str (sum))

if c == "-" :
    difference = float(a) - float(b)
    print("The difference is : " + str (difference))

if c == "/" :
    quotient = float(a) / float(b)
    print("The quotient is : " + str (quotient))

if c == "*" :
    product = float(a) * float(b)
    print("The Product is : " + str(product))