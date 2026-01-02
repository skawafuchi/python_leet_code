from exercise_035.solution import Solution
from collections import Counter

class TestSolution():
    """
    Tests the solution for exercise 35. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()


    def test_example_1(self):
        assert self.solution.searchInsert([1,3,5,6],5) == 2
    
    def test_example_2(self):
        assert self.solution.searchInsert([1,3,5,6],2) == 1

    def test_example_3(self):
        assert self.solution.searchInsert([1,3,5,6],7) == 4

    def test_example_4(self):
        assert self.solution.searchInsert([1,3,5,6],0) == 0
        
    def test_example_5(self):
        assert self.solution.searchInsert([1,3],1) == 0

    def test_example_6(self):
        assert self.solution.searchInsert([1],0) == 0

    def test_example_7(self):
        assert self.solution.searchInsert([1,3],4) == 2

    def test_example_8(self):
        assert self.solution.searchInsert([1,3,5],4) == 2

    def test_example_9(self):
        assert self.solution.searchInsert([1,3,5],6) == 3

    def test_example_10(self):
        assert self.solution.searchInsert([1,3,5],4) == 2

    def test_example_11(self):
        assert self.solution.searchInsert([1,2,3,4,5,10],2) == 1