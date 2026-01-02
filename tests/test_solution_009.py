from exercise_009.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 9. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.isPalindrome(121) is True

    def test_example_2(self):
        assert self.solution.isPalindrome(-121) is False

    def tests_example_3(self):
        assert self.solution.isPalindrome(10) is False

    def tests_example_4(self):
        assert self.solution.isPalindrome(1) is True

    def tests_example_5(self):
        assert self.solution.isPalindrome(313) is True

    def tests_example_6(self):
        assert self.solution.isPalindrome(1000030001) is False
