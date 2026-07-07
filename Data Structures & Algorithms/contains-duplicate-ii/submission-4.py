class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        l = 0
        if k == 0:
            return False

        for i in range(len(nums)):
            if len(window) > k:
                window.remove(nums[abs(i-k)-1])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False