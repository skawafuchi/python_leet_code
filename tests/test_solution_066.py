from exercise_066.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 66. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.plusOne([1, 2, 3]) == [1, 2, 4]

    def test_example_2(self):
        assert self.solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

    def test_example_3(self):
        assert self.solution.plusOne([9]) == [1, 0]

    def test_example_4(self):
        assert self.solution.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6,
                                     7, 0, 5, 5, 4, 3]) == [6, 1, 4, 5, 3, 9,
                                                            0, 1, 9, 5, 1, 8,
                                                            6, 7, 0, 5, 5, 4,
                                                            4]
