class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        bestArea = 0
        
        while l < r:
            area = min(heights[r], heights[l]) * (r - l)
            bestArea = max(bestArea, area)
            smallestBar = min(heights[r], heights[l])
            if smallestBar == heights[r]:
                r -= 1
            else:
                l += 1
        return bestArea

        