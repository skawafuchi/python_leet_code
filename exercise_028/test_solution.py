from solution import Solution
from collections import Counter

class TestSolution():
    """
    Tests the solution for exercise 28. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()


    def test_example_1(self):
        assert self.solution.strStr("sadbutsad","sad") == 0
    
    def test_example_2(self):
        assert self.solution.strStr("leetcode","leeto") == -1
