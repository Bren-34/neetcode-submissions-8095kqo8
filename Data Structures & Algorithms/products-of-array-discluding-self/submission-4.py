class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer =[]
        add = 1
        for i in range(len(nums)):
            for x in nums[0:i]:
                add = add * x
            for y in nums[i+1:len(nums)]:
                add = add * y
            answer.append(add)
            add = 1 
        return answer
