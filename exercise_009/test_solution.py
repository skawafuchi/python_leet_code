from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_1(self):
        assert self.solution.isPalindrome(121) == True
        
    def test_example_2(self):
        assert self.solution.isPalindrome(-121) == False

    def tests_example_3(self):
        assert self.solution.isPalindrome(10) == False

    def tests_example_4(self):
        assert self.solution.isPalindrome(1) == True

    def tests_example_5(self):
        assert self.solution.isPalindrome(313) == True

    def tests_example_6(self):
        assert self.solution.isPalindrome(1000030001) == False