class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            h[num] = 1 + h.get(num, 0)
        
        val = 0
        count = 0
        for key in h:
            if h[key] > count:
                val = key
                count = h[key]
        return val
    

