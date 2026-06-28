class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = []
        count = 0
        for x in nums:
            if x == 1:
                count += 1
            elif x == 0:
                a.append(count)
                count = 0
        a.append(count)
        print(a)
        
        largest = 0
        for x in a:
            if x > largest:
                largest = x
        return largest