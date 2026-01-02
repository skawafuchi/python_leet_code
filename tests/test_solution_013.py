from exercise_013.solution import Solution

class TestSolution():
    """
    Tests the solution for exercise 13. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.romanToInt("III") == 3
        
    def test_example_2(self):
        assert self.solution.romanToInt("LVIII") == 58

    def tests_example_3(self):
        assert self.solution.romanToInt("MCMXCIV") == 1994