# WAF to convert $ to INR

def convert(number):
    rupees = number * 83
    print(rupees)
    return number

Dollar = input("Enter the amount in $ \n")
Dollar = float(Dollar)
convert(Dollar)