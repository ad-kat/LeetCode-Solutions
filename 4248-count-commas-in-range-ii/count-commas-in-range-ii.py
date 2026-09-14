class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        start=1000
        comma=1
        while start<=n:
            end=start*1000-1
            count = min(n, end) - start + 1
            ans += count * comma
            start *= 1000
            comma += 1

        return ans

        