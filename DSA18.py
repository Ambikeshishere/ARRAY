'''
ZIGZAG CONVERSION
'''


class Srivastava:
    def convert(s,numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = ['']*numRows
        current, step = 0,1
        
        for char in s:
            rows [current] += char
            if current == 0:
                step = 1
            elif current ==numRows - 1:
                step = -1
            current += step
        return''.join(rows)

word = input("Enter the word which you want to convert\n")
rows = input("Enter the number of rows in which you want to convert\n")
rows = int(rows)

print(Srivastava.convert(word,rows))