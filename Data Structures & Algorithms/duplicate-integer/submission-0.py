class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenghtlist = len(nums)
        lenghtset = len(set(nums))
        if lenghtlist !=  lenghtset:
            return True
        else:
            return False