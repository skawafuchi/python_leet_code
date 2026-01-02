class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        num_not_matches = 0
        for num in nums:
            if num != val:
                num_not_matches += 1
        nums[:] = [num for num in nums if num != val]
        return num_not_matches