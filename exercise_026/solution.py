class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous_digit = None
        unique_digits = 0
        return_list = []
        for digit in nums:
            if previous_digit is None or previous_digit != digit:
                previous_digit = digit
                unique_digits += 1
                return_list.append(digit)
        nums[:] = return_list
        return unique_digits