class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        # key = number, data = index
        # enumerate throough and add to ans {} and check if there is a match
        for index, num in enumerate(nums):
            # find the goal in relation to the current num
            goal = target - num
            # check if the goal is already in the dict
            if goal in ans:
                # if yes, return the indices of each
                return [ans[goal], index]
            # if not, append current num and index to the dict
            ans[num] = index
            

            