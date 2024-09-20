#Information

info = {
    "name" : "Ambikesh Srivastava",
    "age": 20,
    "is_adult": True,
    "height": 5.6,
    "race": "Black",
    "skills" : {
        "Java" : "Intermediate",
        "Python": 'Advanced',
        "C": "Intermediate",
        "C++": "Basic",
        "HTML": "Advanced",
        "CSS" : "Advanced",
        "JavaScript": "Advanced",
        "ReactJs": "Intermediate"
    }
    }

print(info)
print(info["name"])
info["name"] = "Abhay Raj LALA"

print(info)
print(type(info))
print(info["skills"])
print(info["skills"]["Java"])
print(info.keys())
print(list(info.keys()))
print(len(list(info.keys())))