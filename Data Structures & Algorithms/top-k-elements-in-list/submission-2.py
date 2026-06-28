class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = 1 + count.get(x, 0)


        # bucket sort
        ans = [[] for i in range(len(nums)+1)] 
        for key in count:
            ans[count[key]].append(key)

        res = []
        for i in range(len(ans) -1, 0, -1):
            for n in ans[i]:
                res.append(n)
                if len(res) == k:
                    return res


        