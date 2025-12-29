class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = int(len(nums)/2)
        increment = int(index/2) if len(nums) != 3 else 1
        for i in range(int(len(nums)/2)):
            if nums[index] == target:
                return index
            if nums[index] > target and index > 0:
                index = index - increment
            if index < len(nums)-1 and nums[index] < target:
                index = index + increment
            if nums[index] == target:
                return index
            if increment != 1:
                increment = int(increment/2)
        if index-1 >= 0 and nums[index-1] < target and target < nums[index]:
            return index
        if nums[index] < target:
            return index+1
        
        return 0