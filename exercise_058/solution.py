class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = -1
        split = s.split(" ")
        while (len(split[index]) == 0):
            index-=1
        return len(split[index])