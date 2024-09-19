marks = [87,64,33,95,76]
student = ["Arjun", "Karn", "Duryodhan"]
student[1] = "Yudhisthira"
print(student[0])
print(marks[0])
print(len(marks))
print(len(student))

#lists

marks2 = marks[2:4]
print(marks2)

marks3 = marks[-5:-1]
print(marks3)

marks.append(105)
marks.sort()

print(marks)   

marks.sort(reverse=True)
student.sort(reverse=True)
print(marks)
print(student)
student.sort()
print(student)
print(student)

student.reverse()
print(student)

marks.reverse()
print(marks)

marks.insert(4, "Ambikesh")
print(marks)

student.remove("Duryodhan")
print(student)