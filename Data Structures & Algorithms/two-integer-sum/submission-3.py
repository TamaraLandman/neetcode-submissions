class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        # key = index, data = value
        # enumerate throough and add to ans {} and check if there is a match
        for index, num in enumerate(nums):
            goal = target - num
            if goal in ans:
                return [ans[goal], index]
            ans[num] = index
            

            