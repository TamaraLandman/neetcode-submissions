class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)

        ans = [[] for i in range(len(nums)+1)]
        
        for key in d:
            ans[d[key]].append(key)

        res = []
        for i in range(len(ans) -1, 0, -1) :
            for n in ans[i]:
                res.append(n)
                if k == len(res):
                    return res
                
                     


