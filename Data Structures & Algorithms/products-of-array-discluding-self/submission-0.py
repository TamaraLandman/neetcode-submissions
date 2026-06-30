class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        k = 0 
        product = 1
        while k < len(nums):
            if k != i:
                product *= nums[i] 
            i += 1

            if i == len(nums):
                k += 1
                i = 0
                ans.append(product)
                product = 1

        return ans


        

