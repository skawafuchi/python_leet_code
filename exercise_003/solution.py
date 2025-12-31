class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        longest_str = ""
        for char in s:
            if char not in longest_str:
                if len(longest_str)+1 > longest:
                    longest = len(longest_str)+1
            else:
                longest_str = longest_str[longest_str.index(char)+1:]
            longest_str+=char
        return longest