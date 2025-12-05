class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices_dict = {}
        characters_added_after = {}
        longest = 0
        for letter_index,letter in enumerate(s):
            if letter in indices_dict and indices_dict[letter] != None:
                previous_index = indices_dict[letter]
                if (longest < (letter_index - previous_index)):
                    longest = letter_index - previous_index
                indices_dict[letter] = letter_index
            else:
                indices_dict[letter] = letter_index
                if (letter_index == 1):
                    characters_added_after[s[letter_index-1]] = {letter}
                elif (letter_index > 1):
                    for key in characters_added_after:
                        if (letter in characters_added_after[key]):
                            indices_dict[letter] = None
                        else:
                            characters_added_after[key].add(letter)

        return longest

solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")