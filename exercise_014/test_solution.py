from solution import Solution

class TestSolution():
    solution = Solution()

    def test_example_one(self):
        assert self.solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
        
    def test_example_two(self):
        assert self.solution.longestCommonPrefix( ["dog","racecar","car"]) == ""

    def test_example_3(self):
        assert self.solution.longestCommonPrefix(["ab", "a"]) == "a"