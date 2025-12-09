class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {"(":")","{":"}","[":"]"}
        END_BRACKETS = [")","}","]"]
        open_brackets_list = []
        for bracket in s:
            if bracket not in END_BRACKETS:
                open_brackets_list.append(bracket)
                continue
            if len(open_brackets_list) == 0 or not BRACKET_PAIRS[open_brackets_list.pop()] == bracket:
                return False
        if  len(open_brackets_list) > 0:
            return False
        return True