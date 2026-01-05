class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        combined_digits_string = ""
        for digit in digits:
            combined_digits_string += str(digit)
        digits_plus_one = int(combined_digits_string) + 1
        output = []
        while digits_plus_one > 0:
            output.insert(0, digits_plus_one % 10)
            digits_plus_one = digits_plus_one // 10
        return output
