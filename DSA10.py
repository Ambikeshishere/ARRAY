# Length of Last String
class Ambikesh:
    def Length(s):
        s = s.rstrip()
        words = s.split(" ")
        return len(words[-1])

x = Ambikesh.Length("GOOD MORNING")
print(x)