from exercise_027.solution import Solution
from collections import Counter

class TestSolution():
    """
    Tests the solution for exercise 27. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()


    def test_example_1(self):
        test_list = [3,2,2,3]
        assert self.solution.removeElement(test_list,3) == 2
        assert Counter(test_list) == Counter([2,2])
    
    def test_example_2(self):
        test_list = [0,1,2,2,3,0,4,2]
        assert self.solution.removeElement(test_list,2) == 5
        assert Counter(test_list) == Counter([0,1,4,0,3])