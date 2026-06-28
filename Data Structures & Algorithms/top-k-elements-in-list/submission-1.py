class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = 1 + count.get(x, 0)


        ans = sorted(count, key=lambda x: count[x], reverse=True)
        return ans[0:k]
        