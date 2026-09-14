class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        l=len(nums)
        hashmap={}
        for i in range(0,l):
            k= target - nums[i]
            if k in hashmap:
                return [hashmap[k],i]
            else:
                hashmap[nums[i]]=i
                
        return 0  