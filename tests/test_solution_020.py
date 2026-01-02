from exercise_020.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 20. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.isValid("()") is True
        
    def test_example_2(self):
        assert self.solution.isValid("()[]{}") is True

    def test_example_3(self):
        assert self.solution.isValid("(]") is False

    def test_example_4(self):
        assert self.solution.isValid("([])") is True

    def test_example_5(self):
        assert self.solution.isValid("(") is False

    def test_example_6(self):
        assert self.solution.isValid("((") is False

    def test_example_7(self):
        assert self.solution.isValid("]") is False
