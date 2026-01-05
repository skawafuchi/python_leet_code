from exercise_058.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 58. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.lengthOfLastWord("Hello World") == 5

    def test_example_2(self):
        assert self.solution.lengthOfLastWord("   fly me   to   "
                                              "the moon  ") == 4

    def test_example_3(self):
        assert self.solution.lengthOfLastWord("luffy is still joyboy") == 6
