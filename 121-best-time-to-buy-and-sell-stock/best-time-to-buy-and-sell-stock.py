'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=999999
        best=0
        for i in prices:
            if i<min_so_far:
                min_so_far=i
            else:
                best= max(best, i-min_so_far)
        return best
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxp=0
        while r<len(prices):
            if prices[l]<prices[r]:
                prof=prices[r]-prices[l]
                maxp=max(maxp, prof)
            else:
                l=r
            r+=1
        return maxp
       