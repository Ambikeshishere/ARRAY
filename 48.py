with open("practice.txt", "r") as d:
    data = d.read()
new = data.replace("Java","python")
print(new)


with open("practice.txt", "w") as d:
    d.write(new)