class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_NUMERAL_VALUES = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        last_value = None
        for letter in s:
            if last_value != None and last_value < ROMAN_NUMERAL_VALUES[letter]:
                total -= (last_value*2)
            total += ROMAN_NUMERAL_VALUES[letter]
            last_value = ROMAN_NUMERAL_VALUES[letter]
        return total