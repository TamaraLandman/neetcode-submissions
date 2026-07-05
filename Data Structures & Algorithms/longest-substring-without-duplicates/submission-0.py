class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        d = defaultdict(int)

        for r in range(len(s)):
            d[s[r]] += 1

            while  d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1

            longest = max(longest, r - l +1)
        return longest
            
                

        