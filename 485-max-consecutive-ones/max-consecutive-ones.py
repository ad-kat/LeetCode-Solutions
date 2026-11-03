class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        fans=-999
        ans=0
        for i in nums:
            if i==1:
                ans+=1
            else:                
                fans=max(ans,fans)                
                ans=0
        return max(fans,ans)
        