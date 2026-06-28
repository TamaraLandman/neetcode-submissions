class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        ans = [] * n
        ans = nums + nums
        return ans