class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_for_char = ""
        longest_overall = ""
        for index, char in enumerate(s):
            longest_for_char = char
            index_to_left = index-1
            index_to_right = index+1
            while (True):
                if index_to_left >= 0 and index_to_right < len(s) and \
                        s[index_to_left] == s[index_to_right]:
                    longest_for_char = s[index_to_left:index_to_right+1]
                    index_to_left -= 1
                    index_to_right += 1
                else:
                    break
            if len(longest_for_char) > len(longest_overall):
                longest_overall = longest_for_char

            index_to_left = index-1
            if index_to_left >= 0 \
                    and s[index_to_left] == char:
                index_to_right = index+1
                longest_for_char = s[index_to_left:index_to_right]
                index_to_left -= 1
                while (True):
                    if index_to_left >= 0 and index_to_right < len(s) and \
                            s[index_to_left] == s[index_to_right]:
                        longest_for_char = s[index_to_left:index_to_right+1]
                        index_to_left -= 1
                        index_to_right += 1
                    else:
                        break
            if len(longest_for_char) > len(longest_overall):
                longest_overall = longest_for_char
        return longest_overall