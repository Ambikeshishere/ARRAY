class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.rstrip()
        words = s.split(" ")
        return len(words[-1])

x = Solution.lengthOfLastWord("GOOD MORNING")
print(x)