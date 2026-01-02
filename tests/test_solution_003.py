from exercise_003.solution import Solution

class TestSolution():
    """
    Tests the solution for exercise 3. All values for input and output
    were provided by LeetCode.com
    """
    solution = Solution()
    def test_example_1(self):
        assert self.solution.lengthOfLongestSubstring("abcabcbb") == 3

    def test_example_2(self):
        assert self.solution.lengthOfLongestSubstring("bbbbb") == 1

    def test_example_3(self):
        assert self.solution.lengthOfLongestSubstring("pwwkew") == 3

    def test_example_4(self):
        assert self.solution.lengthOfLongestSubstring(" ") == 1

    def test_example_5(self):
        assert self.solution.lengthOfLongestSubstring("") == 0

    def test_example_6(self):
        assert self.solution.lengthOfLongestSubstring("au") == 2

    def test_example_7(self):
        assert self.solution.lengthOfLongestSubstring("aab") == 2

    def test_example_8(self):
        assert self.solution.lengthOfLongestSubstring("abba") == 2
    
    def test_example_9(self):
        assert self.solution.lengthOfLongestSubstring("dvdf") == 3

    def test_example_10(self):
        assert self.solution.lengthOfLongestSubstring("ckilbkd") == 5

    def test_example_11(self):
        assert self.solution.lengthOfLongestSubstring("bbtablud") == 6