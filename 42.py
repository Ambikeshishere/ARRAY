# WAF to print the elements of a list in a single line. (list is the parameter)

cities = ["Delhi", "Noida", "Prayagraj", "Ahmedabad"]
students = ["Ambikesh", "Abhay", "Aditya", "Arohi", "Pooja", "Devanshi"]

def print_elements(list):
    for item in list:
        print(item, end=" ")
    return list

print_elements(cities)
print("\n")

print_elements(students)

