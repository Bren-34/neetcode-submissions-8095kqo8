class Solution:
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            remainder = target - nums[x]
            if remainder in nums[x+1:]:
                return [x, nums.index(remainder, x+1)]