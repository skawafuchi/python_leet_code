from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_1(self):
        assert self.solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
        
    def test_example_2(self):
        assert self.solution.longestCommonPrefix( ["dog","racecar","car"]) == ""

    def test_example_3(self):
        assert self.solution.longestCommonPrefix(["ab", "a"]) == "a"