from exercise_026.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 26. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        test_list = [1, 1, 2]
        assert self.solution.removeDuplicates(test_list) == 2
        assert test_list == [1, 2]

    def test_example_2(self):
        test_list = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        assert self.solution.removeDuplicates(test_list) == 5
        assert test_list == [0, 1, 2, 3, 4]
