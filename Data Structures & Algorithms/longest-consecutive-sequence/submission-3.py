class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:
             return 0
        ans = [nums[0]]
        d = {}
        size = 1
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i + 1] == nums[i]: continue
            if nums[i+1] - nums[i] == 1:
                ans.append(nums[i+1])
                size += 1
            else:
                d[size] = ans
                ans = [nums[i]]
                size = 1
        d[size] = ans
    
        largest = 0
        res = []
        for key in d:
            if key > largest:
                largest = key
        return largest



        