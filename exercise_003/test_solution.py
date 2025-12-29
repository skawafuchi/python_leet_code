from solution import Solution

class TestSolution():
    """
    Tests the solution for exercise 3. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()
    def test_example_one(self):
        assert self.solution.lengthOfLongestSubstring("abcabcbb") == 3

    def test_example_two(self):
        assert self.solution.lengthOfLongestSubstring("bbbbb") == 1

    def test_example_three(self):
        assert self.solution.lengthOfLongestSubstring("pwwkew") == 3

    def test_example_four(self):
        assert self.solution.lengthOfLongestSubstring(" ") == 1

    def test_example_five(self):
        assert self.solution.lengthOfLongestSubstring("") == 0

    def test_example_six(self):
        assert self.solution.lengthOfLongestSubstring("au") == 2

    def test_example_seven(self):
        assert self.solution.lengthOfLongestSubstring("aab") == 2

    def test_example_eight(self):
        assert self.solution.lengthOfLongestSubstring("abba") == 2
    
    def test_example_nine(self):
        assert self.solution.lengthOfLongestSubstring("dvdf") == 3