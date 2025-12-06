from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_one(self):
        assert self.solution.romanToInt("III") == 3
        
    def test_example_two(self):
        assert self.solution.romanToInt("LVIII") == 58

    def tests_example_three(self):
        assert self.solution.romanToInt("MCMXCIV") == 1994