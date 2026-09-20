'''
import math
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]

        return ans
'''
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[1]*l
        pre=1

        for i in range(0,l):
            ans[i]=pre
            pre=pre*nums[i]
        
        suf=1
        for i in range(l-1,-1,-1):
            ans[i]*=suf
            suf*=nums[i]

        print(ans)
        return ans
