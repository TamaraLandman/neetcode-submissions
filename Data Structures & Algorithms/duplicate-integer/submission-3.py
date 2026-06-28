class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = {}
        for i in nums:
            if i in ans:
                return True
            else: ans[i] = 1
        return False
        # for key in ans:
        #     if ans[key] != 1:
        #         return True
        # return False


        