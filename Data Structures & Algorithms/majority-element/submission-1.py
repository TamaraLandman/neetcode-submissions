class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hMap = {}
        for num in nums:
            hMap[num] = 1 + hMap.get(num, 0)

        largest = 0
        val = 0

        for key in hMap:
            if hMap[key] > largest:
                val = key
                largest = hMap[key]
        
        return val



        