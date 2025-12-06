class Solution:
    #with string conversion
    # def isPalindrome(self, x: int) -> bool:
    #     return str(x) == str(x)[::-1]
    
    #without string conversion
    def isPalindrome(self, x: int) -> bool:
        #negatives can't be palindrones due to the "-"
        if x < 0:
            return False
        #single digit
        if x < 10:
            return True
        digit_list = []
        while x > 0:
            digit_list.append(x%10)
            x = int(x/10)
        for digit_index,digit in enumerate(digit_list):
            if len(digit_list) >= digit_index+1 and digit_list[digit_index] == digit_list[-(digit_index+1)]:
                continue
            return False
        return True