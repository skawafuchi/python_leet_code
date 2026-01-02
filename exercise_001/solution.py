class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for index, num in enumerate(nums):
            sub = target - num
            if sub in map:
                return [map[sub], index]
            else:
                map[num] = index
