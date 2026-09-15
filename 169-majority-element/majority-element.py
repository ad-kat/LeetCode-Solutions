class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        highest_key = max(freq, key=freq.get)
        return highest_key

        