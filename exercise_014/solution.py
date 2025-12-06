class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        for letter_index,letter in enumerate(strs[0]):
            for word in strs:
                if letter_index > (len(word)-1) or letter != word[letter_index]:
                    return common_prefix
            else:
                common_prefix += word[letter_index]
        return common_prefix