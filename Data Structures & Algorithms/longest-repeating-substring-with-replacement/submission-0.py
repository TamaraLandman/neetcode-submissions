class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        l = 0
        d = {}

        longest = 0

        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)

            if (r-l+1) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1

            longest = max(longest, r-l+1)
            
            
        return longest
            
        
        