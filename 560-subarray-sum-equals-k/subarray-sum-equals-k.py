class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}

        curr = 0
        ans = 0

        for num in nums:
            curr += num

            if curr - k in prefix_count:
                ans += prefix_count[curr - k]

            prefix_count[curr] = prefix_count.get(curr, 0) + 1

        return ans