'''
Find the Index of first occurrence in a string.
'''


class Ambikesh:
    def String(str, src):
        try:
            index = str.index(src)
            return index
        except ValueError:
            return -1
        
str = "Hello, this is a haystack containing the word 'needle'."
src = "needle"
result = Ambikesh.String(str, src)
print(f"Index of '{src}' in the haystack: {result}")
