from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_1(self):
        assert self.solution.isValid("()") ==  True
        
    def test_example_2(self):
        assert self.solution.isValid("()[]{}") == True

    def test_example_3(self):
        assert self.solution.isValid("(]") == False

    def test_example_4(self):
        assert self.solution.isValid("([])") == True

    def test_example_5(self):
        assert self.solution.isValid("(") == False

    def test_example_6(self):
        assert self.solution.isValid("((") == False

    def test_example_7(self):
        assert self.solution.isValid("]") == False