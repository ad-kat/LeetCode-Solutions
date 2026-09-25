
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            maxSub=max(maxSub,curr)
        return maxSub
            


