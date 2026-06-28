class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       last = cnt = 0
       for i in nums:
            if i == 1:
                cnt += 1
            else: 
                cnt = 0
            last = max(last, cnt)
       return last

