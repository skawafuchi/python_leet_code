from solution import Solution

class TestSolution():
    """
    Tests the solution for exercise 1. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()

    def test_example_one(self):
        assert self.solution.twoSum(nums=[2,7,11,15],target=9) == [0,1]

    def test_example_two(self):
        assert self.solution.twoSum(nums=[3,2,4],target=6) == [1,2]

    def tests_example_three(self):
        assert self.solution.twoSum(nums=[3,3],target=6) == [0,1]