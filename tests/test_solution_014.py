from exercise_014.solution import Solution


class TestSolution():
    """
    Tests the solution for exercise 14. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_1(self):
        assert self.solution.longestCommonPrefix(["flower", "flow",
                                                  "flight"]) == "fl"

    def test_example_2(self):
        assert self.solution.longestCommonPrefix(["dog", "racecar",
                                                  "car"]) == ""

    def test_example_3(self):
        assert self.solution.longestCommonPrefix(["ab", "a"]) == "a"
