from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_one(self):
        assert self.solution.isPalindrome(121) == True
        
    def test_example_two(self):
        assert self.solution.isPalindrome(-121) == False

    def tests_example_three(self):
        assert self.solution.isPalindrome(10) == False

    def tests_example_four(self):
        assert self.solution.isPalindrome(1) == True

    def tests_example_five(self):
        assert self.solution.isPalindrome(313) == True

    def tests_example_six(self):
        assert self.solution.isPalindrome(1000030001) == False